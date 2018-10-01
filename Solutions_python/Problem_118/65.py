#!/usr/bin/python

import sys, re, string, math, fractions, itertools
from fractions import Fraction
import bisect

ssr = sys.stdin.readline
ssw = sys.stdout.write
def rdline(): return ssr().strip()
def rdstrs(): return ssr.split()
def rdints(): return map(int, ssr().split())



def build_list(m):
    ll = []
    m = (m+1)>>1
    for i in xrange(m):
        ll += build2(i+1)
    return ll


def build2(l):
    n = l * [0]
    s = 0
    ll = build3(l, n, s, 0, 1)
    ll += build3(l, n, s, 0, 2)
    ll += build3(l, n, s, 0, 3)
    return ll

def build3(l, n0, s, i, d):
    n = n0
    ii = l-1-i
    if ii==i:
        s += d*d
    else:
        s += 2*d*d
    if s>9: return []
    n[ii] = n[i] = d
    if i > l-i-3:
        #print >> sys.stderr, intify(n), intify(n)**2
        ss = intify(n)**2
        n[ii] = n[i] = 0
        return [ ss ]
    ll = build3(l, n, s, i+1, 0)
    ll += build3(l, n, s, i+1, 1)
    ll += build3(l, n, s, i+1, 2)
    n[ii] = n[i] = 0
    return ll


def intify(x):
    return int("".join(map(str, x)))
    #return int("".join(map(lambda i: chr(48+i), x)))
    
    
def do_one_case(cnum, fs):
    A,B = rdints()
    n = bisect.bisect_right(fs,B) - bisect.bisect_left(fs,A)
    print "Case #%d: %d" % (cnum, n)


def main():
    fs = build_list(100)
    assert fs==sorted(fs)
    N = int(rdline())
    for i in range(N):
        do_one_case(i+1, fs)


if __name__ == "__main__":
    main()
