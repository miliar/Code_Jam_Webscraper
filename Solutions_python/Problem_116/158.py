import os
import itertools
from python_toolbox.caching.decorators import cache

PROB_NAME = 'tttt'
INPUT_TYPE = 'large'


def winning_set(s):
    return ('.' not in s and
            (('X' in s and 'O' not in s) or ('X' not in s and 'O' in s)))


def solve(case):
    """break 'case', solve and return the solution"""
    grid = case
    # rows
    for i in range(4):
        s = set()
        for j in range(4):
            s.add(grid[i, j])
        if winning_set(s):
            return 'X won' if 'X' in s else 'O won'
    # columns
    for j in range(4):
        s = set()
        for i in range(4):
            s.add(grid[i, j])
        if winning_set(s):
            return 'X won' if 'X' in s else 'O won'
    # major diagonal
    s = set()
    for i, j in [(0, 0), (1, 1), (2, 2), (3, 3)]:
        s.add(grid[i, j])
    if winning_set(s):
        return 'X won' if 'X' in s else 'O won'
    # minor diagonal
    s = set()
    for i, j in [(0, 3), (1, 2), (2, 1), (3, 0)]:
        s.add(grid[i, j])
    if winning_set(s):
        return 'X won' if 'X' in s else 'O won'
    # is the board empty?
    s = set(grid[i, j] for (i, j) in itertools.product(range(4), range(4)))
    if '.' in s:
        return 'Game has not completed'
    return 'Draw'


def read_file(filepath):
    """Read the input file and return a list of cases in a tuple format."""
    cases = []
    with open(filepath, 'rt') as fobj:
        lines = fobj.readlines()
        num_cases = int(lines.pop(0))
        for case in range(num_cases):
            grid = {}
            for i in range(4):
                line = lines.pop(0)
                for j, content in enumerate(c for c in line):
                    grid[i, j] = content
            print grid
            cases.append(grid)
            lines.pop(0)
    return cases


def write_results(results, outfile):
    with open(outfile, 'wt') as f:
        for idx, result in enumerate(results):
            f.write('Case #{}: {}\n'.format(idx + 1, result))


def main(infile, outfile):
    cases = read_file(infile)
    results = [solve(case) for case in cases]
    write_results(results, outfile)

main(os.path.join('io', '{}_{}.in'.format(PROB_NAME, INPUT_TYPE)),
     os.path.join('io', '{}_{}.out'.format(PROB_NAME, INPUT_TYPE)))
