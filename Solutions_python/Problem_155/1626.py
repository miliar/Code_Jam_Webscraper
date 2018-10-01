#!/usr/bin/python

import sys


def readint(f):
    return int(f.readline())


def solve(shyness):
    n = len(shyness)
    shyness = [int(c) for c in shyness]

    cumul = [0]*n
    cumul[0] = shyness[0]

    add = 0
    for i in xrange(1, n):
        if cumul[i-1] < i:
            add += i - cumul[i-1]
            cumul[i-1] = i
        cumul[i] = cumul[i-1] + shyness[i]

    return add

if __name__ == "__main__":
    f = open(sys.argv[1], "r")

    numCases = readint(f)
    for i in xrange(numCases):
        shyness = f.readline().split()[1]
        n = solve(shyness)
        print "Case #%d: %d" % (i + 1, n)
