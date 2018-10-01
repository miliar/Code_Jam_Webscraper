#!/usr/bin/env python3
"""
Google Code Jam
2015 Round 1A

Problem A. Mushroom Monster

written by yamaton in 2015-04-17
"""

def method1(ms):
    return sum(max(i - j, 0) for (i, j) in zip(ms[:-1], ms[1:]))

def method2(ms):
    d = max(i - j for (i, j) in zip(ms[:-1], ms[1:])) # largest dropd = max(max(i - j, 0) for (i, j) in zip(ms[:-1], ms[1:])) # largest drop
    return sum(min(d, m) for m in ms[:-1])

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        _ = input()
        ms = [int(s) for s in input().strip().split()]
        out1 = method1(ms)
        out2 = method2(ms)
        print("Case #%d: %d %d" % ((i + 1), out1, out2))
