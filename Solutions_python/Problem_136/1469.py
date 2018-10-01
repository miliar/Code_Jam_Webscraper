#! /usr/bin/env python

import sys

testcases = int(sys.stdin.readline())

for i in xrange(testcases):
    (farmcost, farmrate, goal) = map(float, sys.stdin.readline().strip().split(' '))
    baserate = 2.0

    t = goal/baserate

    ttf = 0
    fc = 0
    progress = True
    while progress:
        newfarmtime = farmcost / (fc*farmrate + baserate)
        newgoaltime = newfarmtime + ttf + (goal/(baserate + ((fc+1)*farmrate)))

        if newgoaltime < t:
            t = newgoaltime
            ttf += newfarmtime
            fc += 1
        else:
            progress = False


    print "Case #%d: %.07f" % (i+1, t)
