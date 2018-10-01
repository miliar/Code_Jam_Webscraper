#!/usr/bin/env python

import os, sys

def isRecycled (x, y):
    x = str(x)
    y = str(y)

    if len(x) != len(y):
        return False

    for cnum in range(len(x)):
        cstr = x[cnum:] + x[:cnum]
        cstrnum = int(cstr)
        ynum = int(y)
        if cstrnum == ynum:
            return True

    return False

def solve (line):
    num1 = line[0]
    num2 = line[1]

    recCnt = 0
    solvedSet = set()

    for x in range(num1, num2):
        for y in range(x+1, num2+1):
            setCheck1 = "%s,%s" % (str(x), str(y))
            setCheck2 = "%s,%s" % (str(y), str(x))
            if not setCheck1 in solvedSet and not setCheck2 in solvedSet and isRecycled(x, y):
                solvedSet.add(setCheck1)
                solvedSet.add(setCheck2)
                recCnt += 1
    return str(recCnt)


fd = sys.stdin

line = fd.readline()
sets = int(line)+1

for case in range(1, sets):
    line = [int(x) for x in fd.readline().strip().split()]
    nline = solve(line)
    print "Case #%s: %s" % (case, nline)

fd.close()
