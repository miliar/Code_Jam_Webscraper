#!/usr/bin/python

import os
import sys

DEBUG = 0 or os.getenv("DEBUG")

def debug(*what):
    if DEBUG:
        sys.stderr.write("[DEBUG] " + " ".join(map(str, what)) + "\n")

#------------------------------------------------------

def solve_case():
    t = input()
    na, nb = map(int, raw_input().split())
    debug('t', t, 'na', na, 'nb', nb)
    tt = []
    for i in xrange(na + nb):
        j = map(lambda s: map(int, s.split(":")), raw_input().split())
        j[1][1] += t
        j[1][0] += j[1][1] // 60
        j[1][1] %= 60
        #debug('j', j)
        tt.append(map(tuple, j))
    dep_a = sorted(map(lambda p: p[0], tt[:na]))
    arr_a = sorted(map(lambda p: p[1], tt[:na]))
    dep_b = sorted(map(lambda p: p[0], tt[na:]))
    arr_b = sorted(map(lambda p: p[1], tt[na:]))
    debug('dep_a', dep_a)
    debug('arr_a', arr_a)
    debug('dep_b', dep_b)
    debug('arr_b', arr_b)
    sa = sb = 0
    j = 0
    for i in xrange(len(dep_a)):
        if j >= len(arr_b) or arr_b[j] > dep_a[i]:
            sa += 1
        else:
            j += 1
    i = 0
    for j in xrange(len(dep_b)):
        if i >= len(arr_a) or arr_a[i] > dep_b[j]:
            sb += 1
        else:
            i += 1
    return sa, sb

def main():
    for case in xrange(input()):
        debug('case:', case + 1)
        sa, sb = solve_case()
        print "Case #%d: %d %d" % (case + 1, sa, sb)
main()
