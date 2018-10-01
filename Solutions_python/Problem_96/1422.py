#! /usr/bin/python -tt
import sys
import itertools
import math

valid_range = range(0, 11)
pp = ((2, 2), (2, 1), (2, 0), (1, 1), (1, 0), (1, -1), (0, 0), (0, -1), (0, -2), (-1, -1), (-1, -2), (-2, -2))

def build_tuples(p):
    ret = []
    for pi in pp:
        x,y = pi
        if (p - x - y) % 3 != 0:
            continue
        a = (p-x-y)/3
        if (3*a + x + y) != p:
            continue
        r = [a+x, a+y, a]
        if r[0] in valid_range and r[1] in valid_range and r[2] in valid_range:
            r.sort()
            ret.append(tuple(r))
    ss = set(ret)
    return list(ss)

tuples_cache = dict([(i, build_tuples(i)) for i in range(0, 31)])

def solution(inp, nn, ss, pp):
    tt = [tuples_cache[i] for i in inp]

    mmax = []

    for p in itertools.product(*tt):
        supr = 0
        m = 0
        for pi in p:
            a, ax, ay = pi
            if math.fabs(a - ax) == 2 or math.fabs(a - ay) == 2 or math.fabs(ay - ay) == 2:
                supr = supr + 1
            if a >= pp or ax >= pp or ay >= pp:
                m = m + 1
        if supr != ss:
            continue
        mmax.append(m)
        if m == nn:
            return m
    return max(mmax)


def ReadInts(f):
    return map(int, f.readline().strip().split())

f = open(sys.argv[1], 'r')
T = ReadInts(f)[0]
for i in xrange(1, T+1):
    inp = ReadInts(f)
    n, s, p = inp[:3]
    t = inp[3:]
    outp = solution(t, n, s, p)
    print "Case #%d: %s" % (i, outp)
