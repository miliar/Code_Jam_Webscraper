#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import sys

# Internal imports (if any)

def getline():
    return sys.stdin.next().rstrip()

def challenge():
    C, F, X = map(float, getline().strip().split())
    rate = 2.0
    total_time = 0.0
    while True:
        next_farm_time = C / rate
        farm_win_time = C / rate + X / (rate + F)
        win_time = X / rate
        if win_time < farm_win_time:
            total_time += win_time
            break
        total_time += next_farm_time
        rate += F
    print '%.7f' % total_time


# Main entry point
if __name__ == '__main__':
    testcases = int(getline())

    for testcase in xrange(1, testcases + 1):
        print 'Case #%d:' % (testcase, ),
        challenge()

