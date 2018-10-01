#!/usr/bin/python

import os
import sys

#sys.stdin = open('A-test.in', 'r')
#sys.stdout = open('A-test.out', 'w')
#sys.stdin = open('A-small.in', 'r')
#sys.stdout = open('A-small.out', 'w')
#sys.stdin = open('A-small-attempt1.in', 'r')
#sys.stdout = open('A-small-attempt1.out', 'w')
sys.stdin = open('A-large.in', 'r')
sys.stdout = open('A-large.out', 'w')

DEBUG = 1 or os.getenv("DEBUG") == '1'

#if DEBUG:
#    sys.stderr = open('log', 'w')

def debug(*what):
    if DEBUG:
        sys.stderr.write("[DEBUG] " + " ".join(map(str, what)) + "\n")

#-----------------------------------------------------------------------------

for case in xrange(input()):
    debug()
    debug("Case #%d:" % (case + 1))

    P,K,L = map(int, raw_input().split())
#    debug('PKL', P, K, L)
    M = map(int, raw_input().split())
#    debug('M', M)

    if P*K < L:
        debug('Impossible')
        print "Case #%d: Impossible" % (case + 1)
        continue

    M.sort(reverse=True)
    r = 0
    for i in xrange(L):
        r += M[i] * (i // K + 1)
    debug('r', r)
    print "Case #%d: %d" % (case + 1, r)
    
