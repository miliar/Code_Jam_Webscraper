#! /usr/bin/env python

import sys


def solve(line):
    pancake_row = [p == '+' for p in line.split()[0]]
    pan_size = int(line.split()[1])

    flips = 0
    i = 0
    while i < (len(pancake_row) - pan_size + 1):
        if not pancake_row[i]:
            for j in range(i,i + pan_size):
                pancake_row[j] = not pancake_row[j]
            flips += 1
        i += 1

    if all(pancake_row):
        return flips
    return 'IMPOSSIBLE'


def progress(s):
    print("%-80s\r" % s, file=sys.stderr, end='')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        inputfile = sys.argv[1]
    else:
        inputfile = 'input.test'
    with open(inputfile) as f:
        cases = int(f.readline())
        for i in range(cases):
            progress(i)
            line = f.readline().strip()
            print('Case #%d: %s' % (i+1, solve(line)))
