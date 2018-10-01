import os
import time
import pytest
import collections
from contextlib import contextmanager
from typing import List


INPUT_TYPE = 'large'


Case = collections.namedtuple('Case', ['pancakes', 'k'])


def find_first_unhappy(pancakes):
    for index, pancake in enumerate(pancakes):
        if pancake == '-':
            return index
    return None


def flip(pancakes, pancake_num, first_index):
    for i in range(first_index, first_index + pancake_num):
        if pancakes[i] == '-':
            pancakes[i] = '+'
        else:
            pancakes[i] = '-'


def solve(case: Case):
    """break 'case', solve and return the solution"""
    pancakes = list(case.pancakes)
    flips = 0
    while True:
        current_index = find_first_unhappy(pancakes)
        if current_index is None:
            return flips
        if current_index > len(pancakes) - case.k:
            return 'IMPOSSIBLE'
        flips += 1
        flip(pancakes, case.k, current_index)


def read_case(lines: List[str]) -> Case:
    """Read a test case from the input."""
    line = lines.pop(0).split()
    return Case(pancakes=line[0], k=int(line[1]))


def read_file(filepath: str) -> List[Case]:
    """Read the input `filepath` and return a list of cases."""
    cases = []
    with open(filepath, 'rt') as fobj:
        lines = fobj.readlines()
        num_cases = int(lines.pop(0))
        for _ in range(num_cases):
            cases.append(read_case(lines))
    return cases


def write_results(results: List, outfile: str) -> None:
    with open(outfile, 'wt') as f:
        for idx, result in enumerate(results):
            f.write('Case #{}: {}\n'.format(idx + 1, result))


@contextmanager
def timing(prefix):
    start = time.time()
    yield
    print('{} took {} seconds.'.format(prefix, time.time() - start))


def main(infile: str, outfile: str) -> None:
    cases = read_file(infile)
    results = []
    for idx, case in enumerate(cases):
        with timing("Solving case #{}".format(idx + 1)):
            results.append(solve(case))
    write_results(results, outfile)


test_cases = {
    Case('---+-++-', 3): 3,
    Case('+++++', 4): 0,
    Case('-+-+-', 4): 'IMPOSSIBLE',
}


@pytest.mark.parametrize(('case', 'result'), test_cases.items())
def test_function(case: Case, result):
    assert solve(case) == result


if __name__ == '__main__':
    pytest.main(args=[__file__])
    if INPUT_TYPE:
        main(os.path.join('io', '{}.in'.format(INPUT_TYPE)),
             os.path.join('io', '{}.out'.format(INPUT_TYPE)))
