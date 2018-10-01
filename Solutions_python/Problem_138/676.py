#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import sys

# Internal imports (if any)

def getline():
    return sys.stdin.next().rstrip()

def war(nb, kb_):
    kb = kb_[:]
    points = 0
    for b in nb:
        c = (x for x in kb if x > b)
        try:
            kb.remove(c.next())
        except StopIteration:
            points += 1
    return points

def deceitful_war(nb, kb):
    return len(nb) - war(kb, nb)

def challenge():
    no_blocks = int(getline().strip())
    naomi_blocks = sorted(map(float, getline().strip().split())[:no_blocks])
    ken_blocks = sorted(map(float, getline().strip().split())[:no_blocks])
    war_points = war(naomi_blocks, ken_blocks)
    deceitful_war_points = deceitful_war(naomi_blocks, ken_blocks)
    print deceitful_war_points, war_points

# Main entry point
if __name__ == '__main__':
    testcases = int(getline())

    for testcase in xrange(1, testcases + 1):
        print 'Case #%d:' % (testcase, ),
        challenge()

