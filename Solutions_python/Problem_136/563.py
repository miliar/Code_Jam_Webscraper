#! /usr/bin/python

import sys, itertools

def getline():
    return sys.stdin.readline().strip()

DEBUG = False
def out(s):
    if DEBUG:
        sys.stderr.write(str(s) + '\n')

class Case:
    def __init__(self, casenum):
        self.casenum = casenum

    def done(self, answer):
        print 'Case #%d: %0.7f' % (self.casenum, answer)

    def solve(self):
        C, F, X = [float(y) for y in getline().split()]
        farmcost = C
        farmrate = F
        goal = X
        rate = 2.0
        time = goal / rate
        sunk = 0.0
        while True:
            t = sunk + (farmcost / rate) + (goal / (rate + farmrate))
            if t >= time:
                self.done(time)
                return
            sunk += farmcost / rate
            rate += farmrate
            time = t

cases = int(getline())
for case in xrange(cases):
    Case(case + 1).solve()
