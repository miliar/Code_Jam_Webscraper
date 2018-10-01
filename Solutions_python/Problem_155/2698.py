#!/usr/bin/python

import sys

def solve(audience):
    addition = 0
    standing = 0
    for shyness in range(0, len(audience)):
        if standing < shyness:
            addition += shyness - standing
            standing = shyness
        standing += audience[shyness]
    return addition

with open(sys.argv[1], "r") as testFile:
    numQ = int(testFile.readline())
    for q in range(0, numQ):
        data = testFile.readline().split()
        print "Case #%s: %s" % (q + 1, solve(map(lambda x: int(x), list(data[1]))))
    