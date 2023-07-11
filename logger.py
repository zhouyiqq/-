import logging
import colorlog
import os


class MyLogger:
    def __init__(self, logger_name=None):
        foldername = "logfile"
        if not os.path.exists(foldername):
            os.makedirs(foldername)
        if logger_name is None:
            log_file_path = './logfile/log.txt'
        else:
            log_file_path = f"./logfile/{logger_name}.txt"
        # log_format = u"%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
        color_formatter = colorlog.ColoredFormatter(
            "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)",
            log_colors={
                'DEBUG': 'reset',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            },
            reset=True,
            style='%'
        )

        self.logger = logging.getLogger(logger_name)
        # 设置日志
        # 等级总开关的默认级别为WARNING，此处改为DEBUG
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(log_file_path, encoding='utf-8')
        # 设置文件handler的等级
        file_handler.setLevel(logging.INFO)
        # 第三步，定义handler的输出格式
        file_formatter = logging.Formatter(
            "%(asctime)s - %(filename)s[line:%(lineno)d] - pid:%(process)d - tid:%(thread)d - %(levelname)s: %(message)s")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

        # console_handler_added = any(isinstance(
        #     handler, logging.StreamHandler) for handler in self.logger.handlers)
        # if not console_handler_added:
        # 控制台handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(color_formatter)
        self.logger.addHandler(console_handler)

    def debug(self, message, *args):
        # self.logger.debug(message, *args)
        pid = os.getpid()
        if message is None:
            return
        if len(args) > 0:
            self.logger.debug("process [{}] :".format(
                pid) + str(message).format(*args))
        else:
            self.logger.debug("process [{}] :".format(pid) + str(message))

    def info(self, message, *args):
        pid = os.getpid()
        if message is None:
            return
        if len(args) > 0:
            self.logger.info("process [{}] :".format(
                pid) + str(message).format(*args))
        else:
            self.logger.info("process [{}] :".format(pid) + str(message))

    def warning(self, message, *args):
        pid = os.getpid()
        if message is None:
            return
        if len(args) > 0:
            self.logger.warning("process [{}] :".format(
                pid) + str(message).format(*args))
        else:
            self.logger.warning("process [{}] :".format(pid) + str(message))

    def error(self, message, *args):
        pid = os.getpid()
        if message is None:
            return
        if len(args) > 0:
            self.logger.error("process [{}] :".format(
                pid) + str(message).format(*args))
        else:
            self.logger.error("process [{}] :".format(pid) + str(message))

    def critical(self, message, *args):
        self.logger.critical(message, *args)


if __name__ == '__main__':
    logger = MyLogger()
    logger.info('this is a logger info message,{}', 233)
