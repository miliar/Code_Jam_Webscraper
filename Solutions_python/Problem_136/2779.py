from math import ceil


def max_farm(C, F, X):
    farms = int(ceil(X / C - 1 - 2 / F))
    return farms if farms > 0 else 0


def time_for_farm(n, C, F):
    rate = 2.0
    time = 0
    for i in xrange(n):
        time += C / rate
        rate += F
    return time


T = int(raw_input())
for case in xrange(T):
    C, F, X = (float(f) for f in raw_input().split())
    farms = max_farm(C, F, X)
    t1 = time_for_farm(farms, C, F)
    t2 = X / (2.0 + F * farms)
    print 'Case #%d: %f' % (case + 1, t1 + t2)
