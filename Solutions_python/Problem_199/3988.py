#!/usr/bin/env python
import fileinput

import sys

IMPOSSIBLE = 'IMPOSSIBLE'

OPPOSITE = {'+': '-', '-': '+'}


def flip(row, at, flip_size):
    """ Flip starting `at` (numerate from 0)"""
    assert 0 <= at <= len(row)-flip_size
    _ = row
    for i in xrange(at, at+flip_size):
        row = row[:i] + OPPOSITE[row[i]] + row[i + 1:]
    return row


def solve(case):
    # Prepare
    row, flip_size = case.split()
    flip_size = int(flip_size)

    # Algo
    flips = 0
    for i in xrange(0, len(row) - flip_size + 1):
        if row[i] == '+':
            continue
        else:
            row = flip(row, i, flip_size)
            flips += 1
    row_tail = row[len(row) - flip_size:]
    return flips if '-' not in row_tail else IMPOSSIBLE


def extract_cases(inp):
    """ Common googleJam testcases extractor """
    size = int(next(inp))
    cases = []
    for case in inp:
        cases.append(case.strip())

    for i, case in enumerate(cases, 1):
        print('Case #{}: {}'.format(i, solve(case)))


def main():
    assert len(sys.argv) <= 2
    if len(sys.argv) == 2:
        inp = file(sys.argv[1], 'rb')
    else:
        inp = sys.stdin
    extract_cases(inp)


if __name__ == '__main__':
    main()