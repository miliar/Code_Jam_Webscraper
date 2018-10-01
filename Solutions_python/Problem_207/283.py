#!/bin/env python3

# google code jam 2017 round 1B problem 2
# Daniel Scharstein


import sys

sys.setrecursionlimit(5000)

def longestindex(c):
    k = 0
    n = len(c[k])
    for i in [1, 2]:
        if len(c[i]) > n:
            k = i
            n = len(c[k])
    return k

def solve(a):
    N, R, O, Y, G, B, V = a
    #print(N, R, O, Y, G, B, V)
    rs = ["RG"] * G
    ys = ["YV"] * V
    bs = ["BO"] * O
    R -= G
    Y -= V
    B -= O
    if R < 0 or Y < 0 or B < 0:
        return "IMPOSSIBLE"
    rs += ["R"] * R
    ys += ["Y"] * Y
    bs += ["B"] * B
    c = [rs, ys, bs]
    k = longestindex(c)
    #print(c, "longest", k)
    if len(c[k]) < 1:
        return "IMPOSSIBLE"
    s = c[k].pop(0)
    s = find(s, c)
    if s[0] == s[-1]:
        return "IMPOSSIBLE"
    return s

d = {}
d["O"] = 2 # B
d["G"] = 0 # R
d["V"] = 1 # Y
d["R"] = (1, 2)
d["Y"] = (0, 2)
d["B"] = (0, 1)

def find(s, c):
    #print(s, c)
    if c == [[], [], []]:
        return s
    last = s[-1]
    if last in "OGV":
        k = d[last]
        if len(c[k]) < 1:
            return "IMPOSSIBLE"
        s += c[k].pop(0)
        return find(s, c)
    i, j = d[last]
    li = len(c[i])
    lj = len(c[j])
    if li == 0 and lj == 0:
        return s
    if li == 0:
        s += c[j].pop(0)
        return find(s, c)
    if lj == 0:
        s += c[i].pop(0)
        return find(s, c)
    if c[i][0][-1] == s[0]:
        lj -= 1
    if c[j][0][-1] == s[0]:
        li -= 1
    k = i
    if lj > li:
        k = j
    s += c[k].pop(0)
    return find(s, c)

tests = int(input())
for t in range(tests):
    a = map(int, input().split())
    x = solve(a)
    print("Case #%d: %s" % (t+1, x))
