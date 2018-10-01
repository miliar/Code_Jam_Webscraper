#! /usr/bin/env python

import sys
import bisect


def progress(s):
    print("%-80s\r" % s, file=sys.stderr, end='')


def solve2(line):
    initial_free, people = map(int, line.split())
    if initial_free == people:
        return '0 0'
    exp = 0
    while pow(2, exp) <= people:
        exp += 1

    average_space = abs(initial_free - pow(2, exp) + 1)/pow(2, exp)
    empty_spaces = list()
    reminder = 0
    while initial_free > 0:
        x = reminder + average_space
        i = int(x)
        reminder = x - i
        empty_spaces.append(i)
        initial_free -= i + 1
    if len(empty_spaces) < pow(2, exp):
        return '0 0'

    free_empty_spaces = list(zip(*[iter(empty_spaces+[0])] * 2))

    free_empty_spaces.sort(key=lambda couple: max(couple)*2+sum(couple))

    last_position = free_empty_spaces[-(people+1-pow(2, exp-1))]

    return '%s %s' % (max(last_position), min(last_position))




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
            print('Case #%d: %s' % (i+1, solve2(line)))
