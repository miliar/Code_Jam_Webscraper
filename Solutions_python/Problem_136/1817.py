import os
import unittest
from decimal import getcontext, Decimal
getcontext().prec = 20

PROB_NAME = 'cookie_clicker'
INPUT_TYPE = 'large'


def solve(case):
    """break 'case', solve and return the solution"""
    c, f, x = case
    passed_seconds = Decimal(0.0)
    current_rate = Decimal(2.0)
    cookies = Decimal(0.0)

    secs_for_farm = c / current_rate
    secs_for_finish = x / current_rate
    if secs_for_finish < secs_for_farm:
        return secs_for_finish

    secs_for_roi = c / f
    while cookies < x:
        secs_for_farm = (c - cookies) / current_rate
        cookies += current_rate * secs_for_farm
        passed_seconds += secs_for_farm
        secs_for_finish = (x - cookies) / current_rate
        if secs_for_finish < secs_for_roi:
            return passed_seconds + secs_for_finish
        current_rate += f
        cookies -= c


def read_case(lines):
    return [Decimal(num) for num in lines.pop(0).split()]


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


def main(infile, outfile):
    cases = read_file(infile)
    results = [solve(case) for case in cases]
    write_results(results, outfile)


if INPUT_TYPE:
    main(os.path.join('io', '{}_{}.in'.format(PROB_NAME, INPUT_TYPE)),
         os.path.join('io', '{}_{}.out'.format(PROB_NAME, INPUT_TYPE)))


class UnitTest(unittest.TestCase):
    CASES = {}

    def runTest(self):
        message = 'Wrong result for case.\nCase: {}\nResult: {}\n'\
                  'Expected result: {}'
        for case, result in self.CASES.iteritems():
            self.assertEqual(solve(case), result, message.format(case,
                                                                 solve(case),
                                                                 result))
