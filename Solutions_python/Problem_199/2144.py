#!/usr/bin/env python
# -*- coding: utf-8 -*-


def flip(l, k):
    count = 0
    if all(l):
        return 0
    for i, v in enumerate(l):
        if v == False:
            l[i:i+k] = [not s for s in l[i:i+k]]
            count += 1
            if all(l):
                return count
        if i == len(l) - k :
            return "IMPOSSIBLE"

n = int(input())

for i in range(n):
    l = input().split()
    k = int(l[1])
    a = list(map(lambda x: True if x == '+' else False, l[0]))
    ans = flip(a, k)
    print("Case #{0}: {1}".format(i+1 ,ans))


