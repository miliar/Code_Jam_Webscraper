#!/usr/bin/env python

from collections import defaultdict
from math import ceil

T = int(input().strip())
for t in range(T):
    N,R,O,Y,G,B,V = map(int, input().strip().split())
    if N // 2 < max(R,Y,B):
        print("Case #%d: IMPOSSIBLE" % (t+1))
    else:
        S = ''
        for key, cnt in sorted([('R',R),('Y',Y),('B',B)],key=lambda x: x[1], reverse=True):
            S += key*cnt

        size = R + Y + B
        ans = ''
        size = int(ceil(size/2))
        for i in range(size):
            ans += S[i]
            if i+size < len(S):
                ans += S[i+size]

        print("Case #%d: %s" % (t + 1,ans))





