from codejam2014.code_jam_file import CodeJamFile

__author__ = 'tehsphinx'


class CodeJamBase(object):

    def __init__(self):
        pass

    @staticmethod
    def get_cases(file_name):
        jam_file = CodeJamFile(file_name, case_length=10)
        return jam_file.process_file()

    @staticmethod
    def write_result(file_name, result):
        jam_file = CodeJamFile(file_name)
        jam_file.write_result(result)

