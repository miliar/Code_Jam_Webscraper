#!/usr/bin/python2.7

import fileinput
import sys

"""
x=3*n:
n,n,n (1perm)
n-1,n,n+1 (s) (6)

x=3*n+1:
n,n,n+1 (3)
n-1,n+1,n+1 (s) (3)

x=3*n+2:
n,n+1,n+1 (3)
n,n,n+2 (s)(3)
"""

NO = 0
ONLY_WITH_SURPISE = 1
YES = 2

def can(judgesSum, score):
    n = judgesSum / 3
    if judgesSum % 3 == 0:
        if n >= score:
            return YES
        if n == score-1 and n > 0:
            return ONLY_WITH_SURPISE
        else:
            return NO
    elif judgesSum % 3 == 1:
        if n >= score-1:
            return YES
        else:
            return NO
    else: #score % 3 == 2
        if n >= score-1:
            return YES
        elif n == score-2 and n > 0:
            return ONLY_WITH_SURPISE
        else:
            return NO

def runTc(S, p, ts):
    cans = [can(t, p) for t in ts]
    cntOnlyWSurpr = sum([1 if c == ONLY_WITH_SURPISE else 0 for c in cans])
    cntYes = sum([1 if c == YES else 0 for c in cans])
    if cntOnlyWSurpr >= S:
        return S + cntYes
    else:
        return cntOnlyWSurpr + cntYes

def main():
    lineCount = 0
    currTcNo = 0
    noOfTestCases = None
    for line in fileinput.input():
        if lineCount == 0:
            noOfTestCases = int(line)
        else:
            currTcNo += 1
            l = line.strip()
            N, S, p, rest = l.split(" ", 3)
            N, S, p = int(N), int(S), int(p)
            t = [int(x) for x in rest.split(" ")]
            if N != len(t): sys.exit(1)
            print "Case #%d: %s" % (currTcNo, runTc(S, p, t))

        lineCount += 1

if __name__ == '__main__':
    main()
