#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
# c.durr - 2013

# Google Code Jam
# Consonants
# balayage

def readInt():      return int(raw_input())
def readList(type): return map(type, raw_input().split())
def trim(s):        return s.strip(" \t\r\n")
    

def solve(s,n):
    ans  = 0
    a    = 0
    last = -1
    for i in range(len(s)):
        if s[i] in "aeiou":
            last = i
        else:
            if i-last>=n:
                a = i+1-(n-1)
        ans += a
    return ans


for test in range(readInt()):
    [S, N] = raw_input().split()
    s = trim(S)
    n = int(N)
    print 'Case #%d:' % (test+1), solve(s,n)
