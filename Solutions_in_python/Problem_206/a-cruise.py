#!/bin/env python3

# google code jam 2017 round 1B problem 1
# Daniel Scharstein

def solve(d, a):
    #print(d, a)
    y = 1e9999
    for x in a:
        k, s = x
        dd = d - k
        t = dd / s
        if t > 0:
            yy = d / t
            #print(yy)
            y = min(y, yy)
    return y

tests = int(input())
for t in range(tests):
    d, n = map(int, input().split())
    a = []
    for i in range(n):
        k, s = map(int, input().split())
        a.append((k, s))
    x = solve(d, a)
    print("Case #%d: %f" % (t+1, x))
