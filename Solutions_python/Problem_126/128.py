import os
import unittest
import itertools
from python_toolbox.cute_iter_tools import consecutive_pairs

PROB_NAME = 'consonants'
INPUT_TYPE = 'large'

VOWELS = 'aeiou'


def solve(case):
    """break 'case', solve and return the solution"""
    name, n = case
    l = len(name)
    consecutive_consonants = 0
    last_end = 0
    nval = 0
    for idx, c in enumerate(name):
        if c not in VOWELS:
            consecutive_consonants += 1
        else:
            consecutive_consonants = 0
        if consecutive_consonants >= n:
            start, end = idx - n + 1, idx
            if consecutive_consonants > n:
                start_ss = start
            else:
                if n == 1:
                    start_ss = last_end + 1
                else:
                    start_ss = (last_end - n + 2) if last_end > 0 else 0
            end_ss = l
            last_end = end
            left, right = max(start - start_ss + 1, 1), end_ss - end
            nval += left * right
    return nval


def read_case(lines):
    name, n = lines.pop(0).split()
    return (name, int(n))


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
    CASES = {('quartz', 3): 4,
             ('straight', 3): 11,
             ('gcj', 2): 3,
             ('tsetse', 2): 11,
             ('pack', 1): 9}
             # ('packmyboxwithfivedozenliquorjugs', 1): 516}
             # ('z' * 10 ** 6, 4): 0}

    def runTest(self):
        message = 'Wrong result for case.\nCase: {}\nResult: {}\n'\
                  'Expected result: {}'
        for case, result in self.CASES.iteritems():
            self.assertEqual(solve(case), result, message.format(case,
                                                                 solve(case),
                                                                 result))
