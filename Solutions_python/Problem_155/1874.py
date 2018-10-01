"""
Created by bob on 11/04/15
"""

class Reader:
    """
    base reader class
    """

    def __init__(self, filename):
        """
        reads the file and stores as a dictionary of testCases by reading the number of
        test cases and deriving the number of lines per test case . This number of lines
        is read for each test case which is then  stored as a list with each line being
        a string in that list
        """

        def lines_in_file():
            """
            returns the number of lines in the file excluding the first one
            """
            lines = 0
            for line in open(filename):
                lines += 1
            return lines - 1

        self.f = open(filename)
        self.number_test_cases = int(self.f.readline().strip())
        self.test_case_number = 0

    def test_cases(self, fixed_length=None):
        """
        generator to yield testcases
        """
        while self.test_case_number < self.number_test_cases:
            self.test_case_number += 1
            if fixed_length is None:
                descriptors = [int(x) for x in self.f.readline().strip().split(' ')]
            else:
                descriptors = [fixed_length]
            test_case = []
            for number_of_lines in descriptors:
                sub_test_case = []
                for idx in range(number_of_lines):
                    sub_test_case.append(self.f.readline().strip())
                test_case.append(sub_test_case)
            yield (self.test_case_number, test_case)


class Writer:
    """
    class to write the output in the format specified
    """

    def __init__(self, filename, output):
        self.number_cases = len(output)
        with open(filename, 'w') as f:
            for case, result in output.iteritems():
                f.write('Case #' + str(case) + ': ')
                for item in result:
                    f.write(str(item) + ' ')
                f.write('\n')

    def get_number_cases(self):
        return (self.number_cases)


def solver(test):
    """
    solving algoritm for this problem. takes a test case as a list of lists, retruns a solution#
    as a list
    """
    solution = []
    test = test[0][0][2:]
    si_numbers = {}
    idx = 0
    while test != '':
        si_numbers[idx] = int(test[0])
        test = test[1:]
        idx += 1

    standing = 0
    extra = 0
    indexes = sorted(si_numbers.iterkeys())
    for i in indexes:
        if si_numbers[i] and standing < i:
            _extra = i - standing
            extra += _extra
        else:
            _extra = 0
        standing += si_numbers[i] + _extra

    solution.append(extra)

    # main algoritm goes here

    return solution


output = {}
in_filename = 'A-small-attempt5.in'
reader = Reader(in_filename)

for idx, test in reader.test_cases(1):
    output[idx] = solver(test)

out_filename = in_filename[:-2] + 'out'
writer = Writer(out_filename, output)
