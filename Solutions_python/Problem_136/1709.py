from sys import stdin
import sys
sys.setrecursionlimit(10000)
rl = stdin.readline
T = int(rl())


def solve(f):
    if X / f > C / f + X / (f + F):
        return C / f + solve(f + F)

    return X / f


for t in xrange(T):
    C, F, X = map(float, rl().split())
    print 'Case #%d: %.7f' % (t + 1, solve(2.0))

