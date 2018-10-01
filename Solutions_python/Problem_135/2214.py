#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For Codejam 2014
"""

import sys


def readint(fh):
    return int(fh.readline().strip())


def readgrid(fh):
    grid = list()
    for _ in range(4):
        grid.append([int(x) for x in fh.readline().split()])
    return grid


def readrow(fh):
    ans = readint(fh)
    grid = readgrid(fh)
    return grid[ans-1] # zero index

def testcase(fh):
    first = readrow(fh)
    second = readrow(fh)
    ans = set(first).intersection(set(second))
    if len(ans) == 1:
        return ans.pop()
    elif len(ans) > 1:
        return 'Bad Magician!'
    elif not len(ans):
        return 'Volunteer cheated!'
    else:
        raise Exception('Something horrible happened')


def main(args):
    filename = args[1]
    with open(filename) as fh:
        testcases = readint(fh)
        for x in range(1, testcases+1):
            print('Case #{tc}: {ans}'.format(tc=x, ans=testcase(fh)))


if __name__ == '__main__':
    main(sys.argv)
