"""A solution to a Google Code Jam problem.

Each problem is parsed into an arbitrary object (which is different for each
problem). Such objects are called "cases".

To use this template:
1) Implement `read_case(lines)` to parse input lines into a case object.
2) Now that you know how cases look like, write some tests at the bottom of
   the file (copying the sample cases at least).
3) implement `solve(case)` (this is the tricky part!) to return a solution.

Usage:
    gcj [--input=<input> [--output=<output>]]

Options:
    --input=<input-file>        the path to the input file
    --output=<output-file>      the path to the output file

"""

import os
import time
import docopt
import unittest
from contextlib import contextmanager


TEST_CASES = {
    (2, 2, 2): "GABRIEL",
    (2, 1, 3): "RICHARD",
    (4, 4, 1): "RICHARD",
    (3, 2, 3): "GABRIEL",
    (2, 4, 2): "GABRIEL",
    (2, 3, 4): "GABRIEL",
    (2, 1, 1): "RICHARD",
    (4, 3, 4): "GABRIEL",
    (2, 3, 1): "RICHARD",
    (3, 1, 2): "RICHARD",
    (2, 3, 3): "RICHARD",
    (2, 3, 2): "GABRIEL",
    (4, 3, 1): "RICHARD",
    (1, 3, 4): "GABRIEL",
    (3, 2, 1): "RICHARD",
    (4, 1, 4): "RICHARD",
    (4, 1, 1): "RICHARD",
    (4, 3, 3): "RICHARD",
    (3, 3, 1): "RICHARD",
    (4, 1, 2): "RICHARD",
    (1, 4, 2): "GABRIEL",

    (1, 3, 3): "GABRIEL",
    (4, 1, 3): "RICHARD",
    (4, 2, 4): "RICHARD",
    (1, 3, 2): "GABRIEL",
    (2, 1, 2): "GABRIEL",
    (3, 4, 3): "GABRIEL",
    (4, 3, 2): "RICHARD",
    (3, 2, 2): "RICHARD",
    (1, 1, 1): "GABRIEL",
    (2, 4, 1): "GABRIEL",
    (3, 3, 3): "GABRIEL",
    (1, 4, 3): "GABRIEL",
    (4, 4, 2): "RICHARD",
    (3, 2, 4): "RICHARD",
    (3, 4, 2): "RICHARD",
    (4, 4, 3): "GABRIEL",
    (1, 4, 4): "GABRIEL",
    (3, 4, 1): "RICHARD",
    (4, 2, 1): "RICHARD",
    (2, 2, 1): "GABRIEL",
    (2, 2, 4): "GABRIEL",
    (1, 2, 4): "GABRIEL",
    (4, 2, 3): "RICHARD",
    (1, 2, 2): "GABRIEL",
}

def solve(case):
    """break 'case', solve and return the solution"""
    x, r, c = case
    if (r * c) % x != 0:
        return "RICHARD"
    if x >= 7:
        return "RICHARD"
    if r + c < x:
        return "RICHARD"
    if x in (1, 2):
        return "GABRIEL"
    if min(r, c) < (x / 2) + 1:
        return "RICHARD"
    return "GABRIEL"



def read_case(lines):
    """Read input line into a case object.

    This function should `pop` used lines so that `lines` will be ready to
    parse the next case.

    """
    return tuple(int(val) for val in lines.pop(0).split())


def read_file(filepath):
    """Read the input file and return a list of cases in a tuple format."""
    cases = []
    with open(filepath, 'rt') as fobj:
        lines = fobj.readlines()
        num_cases = int(lines.pop(0))
        for _ in range(num_cases):
            cases.append(read_case(lines))
    return cases


def write_results(results, outfile):
    with open(outfile, 'wt') as f:
        for idx, result in enumerate(results):
            f.write('Case #{}: {}\n'.format(idx + 1, result))


@contextmanager
def timing(prefix):
    start = time.time()
    yield
    print '{} took {} seconds.'.format(prefix, time.time() - start)


def main(infile, outfile):
    cases = read_file(infile)
    results = []
    for idx, case in enumerate(cases):
        with timing("Solving case #{}".format(idx + 1)):
            results.append(solve(case))
    write_results(results, outfile)


test_suite = unittest.TestSuite()
for case, result in TEST_CASES.iteritems():
    message = 'Wrong result for case.\nCase: {}\nResult: {}\n' \
              'Expected result: {}'

    class UnitTest(unittest.TestCase):
        def runTest(self, case=case, result=result):
            self.assertEqual(solve(case),
                             result,
                             message.format(case, solve(case), result))

    test_suite.addTest(UnitTest())

if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    assert len(TEST_CASES) > 0, "Don't be an idiot, write some tests!"
    input = args['--input']
    if input:
        output = args['--output'] or input + '.out'
        print input, output
        main(input, output)
    unittest.TextTestRunner().run(test_suite)
