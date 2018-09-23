#!/usr/bin/env python3
import sys

T = int(input())

def naive(N):
    last = 0
    i = N
    while i >= 1:
        s = list(str(i))
        slen = len(s)
        good = 1
        badpos = -1
        for j in range(1, slen):
            if s[j] < s[j - 1]:
                good = 0
                badpos = j - 1
                break
        if good == 1:
            last = i
            break
        else:
            s[badpos] = chr(ord(s[badpos]) - 1)
            for j in range(badpos + 1, slen):
                s[j] = '9'
        s = ''.join(s)
        i = int(s)
    return last

def solve(casei):
    line = input().split(" ")
    N = int(line[0])
    ans = naive(N)
    print("Case #{}: {}".format(casei, ans))

for i in range(1, T+1):
    solve(i)
