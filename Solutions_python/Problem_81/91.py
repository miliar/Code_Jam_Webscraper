from sys import stdin
from collections import defaultdict

def winPercentage(A, ignore = None):
    up = len(wins[A])
    down = len(matches[A])
    if ignore is not None:
        if ignore in wins[A]:
            up -= 1
        if ignore in matches[A]:
            down -= 1
    return 1.0 * up / down

def OWP(A):
    down = len(matches[A])
    up = 0
    for B in matches[A]:
        up += winPercentage(B, A)
    return up/down

def OOWP(A):
    down = len(matches[A])
    up = 0
    for B in matches[A]:
        up += OWP(B)
    return up / down

for caseNo in xrange(1, int(stdin.readline())+1):
    tableSize = int(stdin.readline())
    wins = defaultdict(list)
    matches = defaultdict(list)
    for A in xrange(tableSize):
        for B, ch in enumerate(stdin.readline().strip()):
            if ch == '1':
                wins[A].append(B)
                matches[A].append(B)
            elif ch == '0':
                matches[A].append(B)
    print 'Case #%d:' % caseNo
    for A in xrange(tableSize):
        print 0.25 * winPercentage(A) + 0.5*OWP(A) + 0.25*OOWP(A)
