#!/bin/env python
import sys
import math


def palin(num):
    numstr = str(num)
    for i in range(len(numstr)//2):
        if numstr[i] != numstr[-i-1]:
            return False
    return True


def solvet(f, case):
    low, high = f.readline().split()
    low, high = int(low), int(high)
    count = 0
    high = math.sqrt(high)
    if math.ceil(high) == math.floor(high):
        high = math.ceil(high) + 1
    else:
        high = math.ceil(high)
    low = math.ceil(math.sqrt(low))

    for i in range(low, high):
        if palin(i) and palin(i ** 2):
            count += 1
    print('Case #%d: %d' % (case + 1, count))


def solve(fname):
    with open(fname, 'r') as f:
        numt = int(f.readline())
        for case in range(numt):
            solvet(f, case)


if __name__ == '__main__':
    solve(sys.argv[1])
