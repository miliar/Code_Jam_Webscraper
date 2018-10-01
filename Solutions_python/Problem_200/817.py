#!/usr/bin/env python
# -*- coding: utf-8 -*-
from IPython import embed

def replace_after_zero(d):
    for i in range(len(d)):
        if d[i] == 0:
            d[i-1]-=1
            idx = i
            while idx < len(d):
                d[idx]=9
                idx+=1
    return d

def d2l(x):
    return [int(x) for x in str(cipher)]

def l2d(numList):
    return int(''.join(map(str,numList)))


def solve(d):
    d = d2l(d)

    if is_tidy(d):
        return str(l2d(d))

    d = replace_after_zero(d)

    for i in range(len(d)-1, 0, -1):
        if d[i-1] > d[i]:
            idx = i
            d[i-1] -= 1
            while idx < len(d):
                d[idx]=9
                idx+=1

    return str(l2d(d))


def is_tidy(d):
    if len(d)==1:
        return True

    for i in range(len(d) - 1):
        if d[i] > d[i+1]:
            return False
    return True

if __name__ == "__main__":
    testcases = input()
    #testcases = [15327, 52613, 1372501231]
    for caseNr in xrange(1, testcases+1):
    #for caseNr in xrange(1, len(testcases)+1):
        #cipher = testcases[caseNr-1]
    #    embed()
        cipher = raw_input()
        #print(cipher)
        print("Case #%i: %s" % (caseNr, solve(cipher)))
