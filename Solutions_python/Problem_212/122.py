#!/usr/bin/python

def findMax(P, G):
    r = [0 for i in range(P)]
    for g in G:
        r[g % P] += 1
        
    total = r[0]
    r[0] = 0
    for i in range(1, (P + 2) // 2):
        if i == P / 2:
            pairs = r[i] // 2
            total += pairs
            r[i] -= pairs * 2
        else:
            pairs = min(r[i], r[P - i])
            total += pairs
            r[i] -= pairs
            r[P - i] -= pairs
    for rr in r:
        total += (rr + P - 1) // P
    return total

T = int(raw_input())
for t in range(T):
    N, P = list(map(int, raw_input().split()))
    G = list(map(int, raw_input().split()))

    n = findMax(P, G)
    print("Case #%d: %s" % (t + 1, n))