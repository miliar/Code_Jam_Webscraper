__author__ = 'hansihe'


def fixed_length_case_reader(length=1, extra_newline=False):
    def case_reader(case_num, file):
        result = [file.readline().rstrip() for line_num in range(0, length)]
        if extra_newline:
            file.readline()
        return result
    return case_reader


def read_test_file(file, case_reader):
    num_cases = int(file.readline().rstrip())

    for case_num in range(1, num_cases+1):
        yield case_num, case_reader(case_num, file)