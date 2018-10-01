#!/usr/bin/python
import os, sys

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a < b:
        t = a
        a = b
        b = t
    #divide, etc.
    while b > 0:
        q = a / b
        r = a - q * b
        a = b
        b = r
    return a

def solve(ts):
    # First, find the GCD of all their differences.
    gcdAccum = 0
    differences = [abs(ts[i] - ts[i+1]) for i in range(len(ts)-1)]
    #print differences
    for i in range(len(differences)):
        gcdAccum = gcd(gcdAccum, differences[i])
    #print gcdAccum
    # Find the next time the first one will be at a multiple of that
    if gcdAccum == 0:
        # All are the same
        return 0
    q = ts[0] / gcdAccum
    nextTime = (q+1) * gcdAccum - ts[0]
    if q * gcdAccum == ts[0]:
        return 0
    else:
        return nextTime

def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        caseStr = fileLines[index][:-1]
        index += 1
        ts = [int(x) for x in caseStr.split(' ')][1:]
        #print caseStr
        #print ts
        t = solve(ts)
        print "Case #%d: %d" % (caseNum + 1, t)

if __name__ == '__main__':
    main(sys.argv[1])
