#!/usr/bin/env python

T = int(input())

for t in range(1, T+1):
    print("Case #"+str(t)+": ", end="")

    line = input().split()
    A = int(line[0])
    B = int(line[1])
    K = int(line[2])

    res = 0
    for a in range(A):
        for b in range(B):
            if a&b < K:
                res += 1

    print(res)
