#!/usr/local/bin/python

import sys
from bisect import bisect_left

T = int(sys.stdin.readline())


def play_war(A, B):
    B = B[:]

    idx = len(A) - 1
    point = 0

    while idx >= 0:
        try:
            i = B[bisect_left(B, A[idx])]
        except IndexError:
            i = B[0]

        if A[idx] > i:
            point += 1

        B.remove(i)
        idx -= 1

    return point

def play_dwar(A, B):
    startA = 0
    endA   = len(A) - 1

    startB = 0
    endB   = len(B) - 1

    point = 0

    for i in xrange(len(A)):
        match = None
        if A[i] < B[startB]:
            #print "%d : %.3f -> %.3f" % (point, A[i], B[endB])
            endB -= 1
        else :
            point  += 1
            #print "%d : %.3f -> %.3f" % (point, A[i], B[startB])
            startB += 1
    return point


for caseno in xrange(T):
    N = int(sys.stdin.readline())
    A = [float(x) for x in sys.stdin.readline().split()]
    B = [float(x) for x in sys.stdin.readline().split()]

    A = sorted(A)
    B = sorted(B)

    fair = play_war(A, B)
    cheat = play_dwar(A, B)

    print "Case #%d: %d %d" % (caseno + 1, cheat, fair)
