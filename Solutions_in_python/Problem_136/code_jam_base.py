from codejam2014.code_jam_file import CodeJamFile

__author__ = 'tehsphinx'


class CodeJamBase(object):
    case_length = 1

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def solve(self, cases):
        raise Exception('overwrite this function!')

    def process(self):
        cases = self.get_cases(self.input_file)
        result = self.solve(cases)
        self.write_result(self.output_file, result)

        return result

    def get_cases(self, file_name):
        jam_file = CodeJamFile(file_name, case_length=self.case_length)
        return jam_file.process_file()

    @staticmethod
    def write_result(file_name, result):
        jam_file = CodeJamFile(file_name)
        jam_file.write_result(result)

