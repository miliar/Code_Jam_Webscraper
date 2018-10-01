#!/usr/bin/python

import sys

def readfloats(f):
    return [float(s) for s in f.readline().split()]

def readint(f):
    return int(f.readline())

def cookie(f):
    rate = 2.
    cook = 0.
    time = 0.
    cost, up, goal = readfloats(f)

    while cook < goal:
        time += cost / rate
        cook += cost

        left = goal - cook
        timeToGo = left / rate

        newRate = rate + up

        if (left + cost) / newRate < timeToGo:
            cook = 0
            rate += up
        else:
            time += left / rate
            cook = goal

    return time

if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    numCases = readint(f)
    for i in xrange(numCases):
        print "Case #%d: %.7f" % (i + 1, cookie(f))
