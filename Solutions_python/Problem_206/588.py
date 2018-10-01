#!/usr/bin/env python


T = int(raw_input().strip())
for t in range(T):
    D, N = [int(x) for x in raw_input().strip().split()]
    tmin = 0.0
    for n in range(N):
        K, S = [float(x) for x in raw_input().strip().split()]
        if K < D:
            tt = (D-K) / S
            if tt > tmin:
                tmin = tt
    print 'Case #%d: %s' % (t+1, D / tmin)
