#! /usr/bin/python
import sys
#from decimal import Decimal
from fractions import Fraction

def main():
    T = input()
    for i in xrange(1, T + 1):
        print 'Case #%d:' % i,
        X, S, R, t, N = map(int, raw_input().split())
        walkways = [map(int, raw_input().split()) for j in xrange(N)]
        print '%.6f' % solve2(X, S, R, t, walkways)

def solve2(X, S, R, t, walkways):
    passages = []
    pos = 0
    for B, E, w in walkways:
        if B > pos:
            passages.append((B - pos, 0))
        passages.append((E - B, w))
        pos = E
    if pos < X:
        passages.append((X - pos, 0))

    passages.sort(key=lambda (delta, v): v)

    acc = Fraction(0)
    runtime = Fraction(t)
    for delta, v in passages:
        if runtime:
            Sa = runtime * (v + R)
            if Sa > delta:
                rtime = Fraction(delta, v + R)
                assert rtime < runtime
                runtime -= rtime
                acc += rtime
            else:
                Sb = delta - Sa
                acc += runtime + Fraction(Sb, v + S)
                runtime = 0
        else:
            acc += Fraction(delta, v + S)
    return acc

if __name__ == '__main__':
    sys.exit(main())
