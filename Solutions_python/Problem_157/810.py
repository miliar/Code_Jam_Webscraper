#!/usr/bin/env python
# encoding: utf-8

import sys
import math

inFileName = sys.argv[1]
outFileName = sys.argv[2]

matrix = [[1, 2, 3, 4],
          [2, -1, 4, -3],
          [3, -4, -1, 2],
          [4, 3, -2, -1]]
matrixMap = {"i": 2, "j": 3, "k": 4}


def calc(x, lgstring):

    if len(lgstring) == 1:
        return False

    lgstring = [matrixMap[c] for c in lgstring]
    lgstring = lgstring * x

    if len(lgstring) < 3:
        return False

    #print("len: %d" % len(lgstring))
    lenString = len(lgstring)

    kArray = genArray(list(reversed(lgstring)), matrixMap["k"], left=False)
    # reverse indexes in k
    kArray = list(map(lambda x: lenString - x - 1, kArray))

    cSum = 1
    lastI = -1
    for i, c in enumerate(lgstring):
        cSum = multi(cSum, c)
        if cSum == 2 and lastI < 0:
            lastI = i
            cSum = 1
        if cSum == 3 and lastI >= 0 and i + 1 < lenString:
            #walkToEnd = calcSubstring(lgstring, i + 1, lenString)
            #if walkToEnd == 4:
            if i + 1 in kArray:
                return True
    return False


def calcSubstring(substr, start, end):
    chain = 1
    for c in range(start, end):
        c = substr[c]
        chain = multi(chain, c)
    return chain


def multi(chain, c):
    sign = int(math.copysign(1, chain) * math.copysign(1, c))
    return matrix[abs(chain) - 1][abs(c) - 1] * sign


def genArray(lgstring, matchChar, left=True):
    iChain = 1
    iArray = []
    for i, iChar in enumerate(lgstring[0:-2]):
        if left:
            iChain = multi(iChain, iChar)
        else:
            iChain = multi(iChar, iChain)
        if iChain == matchChar:
            iArray.append(i)
    return iArray

with open(inFileName, "r") as inFile, open(outFileName, "w") as out:
    header = inFile.readline()
    nrCases = int(header)
    lines = inFile.readlines()
    for i, (nrs, lgstring) in enumerate(zip(lines[::2], lines[1::2])):
        if i >= nrCases:
            print("overflow")
            break
        nrs = list(map(int, nrs.strip().split(" ")))
        x = nrs[1]
        lgstring = lgstring.strip()
        if nrs[0] != len(lgstring):
            print("invalid data")
        lsg = calc(x, lgstring)
        lsg = "YES" if lsg else "NO"
        print("Case #%d: %s" % (i + 1, lsg))
        print("Case #%d: %s" % (i + 1, lsg), file=out)
