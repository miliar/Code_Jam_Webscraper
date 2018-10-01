from collections import Counter
import fileinput
import math

def debug(msg):
    if False:
        print msg

class TestCaseRunner():
    def __init__(self, lines_per_test_case=1):
        self.lines = lines_per_test_case
        self.infile = fileinput.input()

        # Get number of testcases
        self.num_tests = int(self.nextline())
        self.filename = self.infile.filename()
        outfile = self.filename.replace(".in", "") + ".out"
        self.output = open(outfile, "w")

        print "%s testcases. Outputting to %s" % (self.num_tests, outfile)

    def nextline(self):
        return next(self.infile)

    def run(self, solve, limit = None):
        if limit is None:
            limit = self.num_tests
        for case in xrange(1, limit + 1):
            if self.lines == 1:
                testcase = self.nextline().replace("\n","")
            else:
                testcase = []
                for _ in xrange(self.lines):
                    testcase.append(self.nextline().replace("\n",""))

            result = solve(testcase)
            self.output_result(case, result)

    def output_result(self, case, result):
        self.output.write("Case #%s: %s\n" % (case, result))

class TestCase():
    def __init__(self, input):
        assert len(input) == 2
        self.num_diners = int(input[0])
        self.num_pancakes = []
        tmp = {}
        for rv in input[1].split(" "):
            self.num_pancakes.append(int(rv))
        self.pancake_counter = Counter(self.num_pancakes)
        self.pancake_list = self.pancake_counter.keys()
        self.pancake_list.sort()
        self.pancake_list.reverse()

        debug("Test case %s" % input[1])

    def solve(self):
        best = 1500
        for target in xrange(1, self.pancake_list[0] + 1):
            debug(">>>>Trying for target %s" % target)
            rv = self.solve_for_target(target)
            debug(">>>>>>Got %s specials, making total %s" % (rv, rv + target))
            if rv + target < best:
                best = rv + target
        debug(">>Best is %s" % best)
        return best

    def solve_for_target(self, target):
        num_specials = 0
        for i in xrange(0, len(self.pancake_list)):
            num_pancakes = self.pancake_list[i]

            if num_pancakes <= target:
                # Reached our target
                break

            num_splits = int(math.ceil(num_pancakes / float(target)) - 1)

            num_specials += num_splits * self.pancake_counter[num_pancakes]

        return num_specials



def solve(input):
    tc = TestCase(input)
    return tc.solve()



if __name__ == '__main__':
    runner = TestCaseRunner(2)
    runner.run(solve)
