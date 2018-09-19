import sys


def xtime(nfarms, c, f, x):
    t = x/(2 + nfarms*f) + ftime(c, f, nfarms)
    return t

def ftime(c, f, nfarms):
    res = 0
    for i in xrange(nfarms):
        res += c/(2 + f*(nfarms - i - 1))
    return res

def best_time(c ,f, x):
    t = float("inf")
    n = 0
    while 1:
        t2 = xtime(n, c, f, x)
        if t2 > t:
            return t
        n += 1
        t = t2

T = int(sys.stdin.readline())
for i in xrange(1, T + 1):

    C, F, X = map(float, sys.stdin.readline().split())
    print 'Case #%s: %s' % (i, best_time(C, F, X))