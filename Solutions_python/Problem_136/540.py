#!/usr/bin/env python3

# C cookies to buy a farm
# F cookies/per second for a farm
# X goal
# N number of farms
def when(C, F, X, N):
    return X/(2 + N * F)


T = int(input())
for t in range(1, T+1):
    C, F, X = map(lambda x:float(x), input().split())
    best = when(C, F, X, 0)
    farm_time = 0
    N = 0
    while True:
        farm_time += when(C, F, C, N)
        new = farm_time + when(C, F, X, N+1)
        if new > best:
            break
        N = N + 1
        best = new
    print("Case #%d: %.7f" % (t, best))
