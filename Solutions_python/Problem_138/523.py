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

    def done(self, war, dwar):
        print 'Case #%d: %d %d' % (self.casenum, dwar, war)

    def solve(self):
        b = int(getline())
        n = [float(x) for x in getline().split()]
        k = [float(x) for x in getline().split()]
        n.sort()
        k.sort()
        w = self.war(n[:], k[:])
        dw = self.dwar(n[:], k[:])
        self.done(w, dw)

    def war(self, n, k):
        wins = 0
        beat = False
        for x in n:
            for y in k:
                if y > x:
                    k.remove(y)
                    beat = True
                    break
            if beat:
                beat = False
            else:
                wins += 1
                del k[0]
        return wins

    def dwar(self, n, k):
        wins = 0
        while n:
            if n[0] > k[0]:
                wins += 1
                del n[0]
                del k[0]
            else:
                del n[0]
                del k[-1]
        return wins + len(n)

cases = int(getline())
for case in xrange(cases):
    Case(case + 1).solve()
