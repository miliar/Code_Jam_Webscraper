#!/usr/bin/env python

T = int(input().strip())
for t in range(T):
    D,N = map(int, input().strip().split())
    _max_time = 0
    for i in range(N):
        K,S = map(int, input().strip().split())
        _max_time = max(_max_time, (D-K)/S)

    print("Case #%d: %f" % (t+1, D/_max_time))




