#!/usr/bin/env python

import sys

def parseInput(inputfile):
    lines = [item.strip() for item in open(inputfile).readlines()]
    t = int(lines[0])
    lines = lines[1:]
    return (t, lines)

def printResult(case, result):
    print("Case #%s: %s" % (case,result))

def genTriplet(score):
    score1 = score2 = score3 = score // 3
    r = score % 3
   
    return (r, (score1, score2, score3))

inputfile = sys.argv[1]
t, lines = parseInput(inputfile)
for index in range(1,t+1):
    result = 0
    line = [int(item) for item in lines[index-1].split()]
    N = line[0]
    S = line[1]
    P = line[2]
    scores = line[3:]
    for score in scores:
        r, triplet = genTriplet(score)
        if max(triplet) >= P:
            result += 1
        else:
            if r == 0 and max(triplet) > 0:
                if S > 0:
                    if max(triplet) + 1 >= P:
                        result += 1
                        S -= 1
            elif r == 1:
                if max(triplet) + 1 >= P:
                    result += 1
            elif r == 2:
                if max(triplet) + 1 >= P:
                        result += 1
                elif S > 0:
                    if max(triplet) + 2 >= P:
                        result += 1
                        S -= 1
    
    printResult(index, result) 
