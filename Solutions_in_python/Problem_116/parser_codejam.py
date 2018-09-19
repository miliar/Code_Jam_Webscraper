# coding: utf-8


class AbstractParser(object):
    def __init__(self, input_path, output_path='solutions.txt'):
        self.input_path = input_path
        self.output_path = output_path
        self.result = []

    def parse_line(self, line):
        raise AssertionError("Not implemented")

    def parse(self):
        parsed_case = []
        with open(self.input_path) as file:
            lines = file.readlines()
            n, lines = int(lines[0]), lines[1:]
            assert(not lines[-1].strip())  # hay newline al final
            for line in lines:
                line = line.strip()
                if line:
                    parsed_case.append(self.parse_line(line.strip()))
                else:
                    self.result.append(parsed_case)
                    parsed_case = []
            assert(n == len(self.result))

            return self.result
