#!/usr/bin/env python3

t = int(input())
for i in range(1, t + 1):
    S, K = input().split()
    S = [{'+': 1, '-': -1}[i] for i in S]
    K = int(K)

    tries = 0
    for ii in range(0, len(S) + 1 - K):
        first = S[ii]
        if first == -1:
            tries += 1
            S[ii:ii+K] = [z * -1 for z in S[ii:ii+K]]
        if all(i == 1 for i in S):
            print("CASE #{}: {}".format(i, tries))
            break
    else:
        print("CASE #{}: IMPOSSIBLE".format(i))

