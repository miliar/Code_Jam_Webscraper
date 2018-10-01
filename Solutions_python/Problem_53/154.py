#!/usr/bin/python
import os, sys

def snap(n, k):
    return (k > 0) and ((k+1) % pow(2,n) == 0)

def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        caseStr = fileLines[index][:-1]
        index += 1
        (n, k) = [int(x) for x in caseStr.split(' ')]
        #print caseStr
        answer = snap(n, k)
        print "Case #%d: %s" % (caseNum + 1, 'ON' if answer else 'OFF')

if __name__ == '__main__':
    main(sys.argv[1])
