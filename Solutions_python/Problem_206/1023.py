#!/usr/bin/env python3

def solve():
    return 0

for i in range(int(input().strip())):
    d, n = map(int,input().strip().split())
    max_t = 0
    for _ in range(n):
        k, s = map(int, input().strip().split())
        max_t = max(max_t, ((d-k)/s))
    print("Case #{}: {}".format(i+1, d/max_t))

