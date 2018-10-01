class TestCase:
    id = 1

    def __init__(self, n):
        self.n = n

        TestCase.id += 1

    @staticmethod
    def parse(line):
        return TestCase(line.strip())

def parse():
    import sys
    fh = open(sys.argv[1])
    testcase_count = int(fh.readline())

    testcases = []
    for i in range(testcase_count):
        testcases.append(TestCase.parse(fh.readline()))

    return testcases

def get_biggest_tidy_substring(number):
    for i in range(1, len(number)):
        if number[i] < number[i - 1]:
            return number[:i]
    return number

def reduce_number_by_one(number):
    if number[-1] == '0':
        return reduce_number_by_one(number[:-2]) + '9'
    if number == '0':
        return ''
    return remove_leading_zeros(number[:-1] + str(int(number[-1]) - 1))

def remove_leading_zeros(number):
    while len(number) > 0 and number[0] == '0':
        number = number[1:]
    return number

def calculate(testcase):
    while True:
        substring = get_biggest_tidy_substring(testcase.n)

        if len(testcase.n) != len(substring):
            testcase.n = reduce_number_by_one(substring) + '9' * (len(testcase.n) - len(substring))
        else:
            return testcase.n

def main():
    testcases = parse()
    i = 1
    for testcase in testcases:
        print "Case #%d: %s" % (i, calculate(testcase))
        i += 1

if __name__ == '__main__':
    main()
