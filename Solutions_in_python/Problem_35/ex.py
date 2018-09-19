#!/usr/bin/env /usr/bin/python
# -*- coding: utf-8 -*-

import sys

import land

fileHandle = sys.stdin if (len(sys.argv) == 1 or sys.argv[1] == '-') else open(sys.argv[1])

testCases = int(fileHandle.readline().strip())

for i in range(1, testCases + 1):
    testCase = land.Land.createFromGCJExerciseFile(fileHandle)
    
    print "Case #%d:" % i
    
    for x in range(0, testCase.hw[0]):
        for y in range(0, testCase.hw[1]):
            testRegion = testCase.getFromXY((x,y))
            
            while not testRegion.isSink():
                testRegion = testRegion.getMaxNearRegion()
            
            out = ("%s" if y == testCase.hw[1] - 1 else "%s ")
            
            sys.stdout.write(out % testRegion.getSinkName())
            
        sys.stdout.write("\n")

fileHandle.close()

