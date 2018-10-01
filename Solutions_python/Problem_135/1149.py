import os
from codejam2014.functions import dbg

__author__ = 'tehsphinx'


class CodeJamFile(object):
    def __init__(self, file_name, case_length=0):
        self.file_name = file_name
        self.case_length = case_length

        self.lines = []
        self.cases_amount = 0
        self.cases = {}

    def process_file(self):
        path = os.path.dirname(os.path.realpath(__file__)) + '/' + self.file_name + '.txt'
        dbg(input=path)
        self.lines = self.read_file(path)

        self.cases_amount = int(self.lines[0])

        return self.process_cases()

    def process_cases(self):
        if self.case_length > 0:
            self.cases = {}
            for case_number in range(1, self.cases_amount + 1):
                case = []
                for case_line in range(1, self.case_length + 1):
                    case.append(self.lines[(case_number - 1) * self.case_length + case_line].replace('\n', ''))
                self.cases[case_number] = case

        return self.cases

    def write_result(self, result: dict):
        path = os.path.dirname(os.path.realpath(__file__)) + '/' + self.file_name + '.txt'
        dbg(output=path)

        self.write_file(path, result.values())

    @staticmethod
    def read_file(path):
        file = open(path, 'r+')
        lines = file.readlines()
        file.close()

        return lines

    @staticmethod
    def write_file(path, lines):
        output_lines = [x + '\n' for x in lines]

        file = open(path, 'w+')
        file.writelines(output_lines)
        file.close()
