#!/usr/bin/python

import sys

def readints(f):
    return [int(s) for s in f.readline().split()]
def readint(f):
    return int(f.readline())

table = {}
sums = {}
happies = {}

def isHappy(number, base):
    if (number, base) in table:
        return table[(number, base)]
    s = 0
    previousNumbers = []
    while True:
        s = 0
        if (number, base) in sums:
            s = sums[(number, base)]
        else:
            n = number
            while n > 0:
                d = n % (base)
                s += d*d
                n = n / base
            sums[(number, base)] = s
        if s == 1:
            if base not in happies:
                happies[base] = [number]
            else:
                happies[base] += [number]
            table[(number, base)] = True
            return True
        if s in previousNumbers:
            table[(number, base)] = False
            return False
        if (s, base) in table:
            hap = table[(s, base)]
            if hap:
                if base not in happies:
                    happies[base] = [number]
                else:
                    happies[base] += [number]            
            return hap 
        number = s
        previousNumbers += [s]        

def findHappy(bases):
    test = 2
    found = False
    while not found:
        numHappy = 0
        found = True
        for base in bases:
            if not isHappy(test, base):
                found = False
                continue
        if found:
            return test
        test += 1        
    return -1
        

if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    numCases = readint(f)
    for i in xrange(numCases):
        bases = readints(f)
        print "Case #%d: %d" % ((i + 1), findHappy(bases))
