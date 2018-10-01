#!/usr/bin/env python3

import operator


def solve(d, horses):
    times = map(lambda h: (d - h[0]) / h[1], horses)
    return d / max(times)

if __name__ == "__main__":
    t = int(input())
    for i in range(1, t + 1):
        h = []
        d, n = map(int, input().split())
        for j in range(n):
            h.append(list(map(int, input().split())))
        print("Case #{}: {}".format(i, solve(d, h)))
