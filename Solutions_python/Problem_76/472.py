#!/usr/bin/env python
# encoding: utf-8
"""
problemC.py

Created by Joshua Olson on 2011-05-05.
Copyright (c) 2011 solarmist. All rights reserved.
"""

import sys
import os

def xor(l):
    return reduce(lambda x, y: x ^ y, l)

def toInt(l):
    return map(lambda x: int(x), l)

def sum(l):
    return reduce(lambda x, y: x + y, l)

def main():
    data = sys.stdin.readlines()
    cases = int(data.pop(0))
    for case in range(cases): #line is an int containing the index of the case
        print 'Case #' + str(case + 1) + ':',
        numCandies = int(data.pop(0))
        caseData = data.pop(0).split()
        caseData = toInt(caseData)
        #xor all data to get the solvability
        solve = xor(caseData)
        
        caseData.sort()
        
        if solve != 0:
            print 'NO'
            continue
        
        patTotal = 0
        seanTotal = 0
        for x in range(len(caseData)):
            candy = caseData.pop(0)
            if patTotal ^ candy != 0:
                patTotal ^= candy
            else:
                caseData.append(candy)
                
            if patTotal ^ xor(caseData) == 0:
                seanTotal = sum(caseData)
                break
        print seanTotal

if __name__ == '__main__':
	main()

