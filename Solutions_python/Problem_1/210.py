#!/usr/bin/env python import sys
import sys

def calc_switch_cnt(engines, queries) :
    result = 0
    engfit = list(engines)
    for q in queries :
        if q in engfit :
            if len(engfit) == 1 : #increase count
                result += 1
                engfit = list(engines)
            engfit.remove(q)
    return result


cnt = int(sys.stdin.readline())
for i in xrange(cnt):
    eng_cnt = int(sys.stdin.readline())
    engines = [sys.stdin.readline() for j in xrange(eng_cnt)]
    q_cnt = int(sys.stdin.readline())
    queries = [sys.stdin.readline() for j in xrange(q_cnt)]
    print 'Case #%d: %d' % (i + 1, calc_switch_cnt(engines, queries))
