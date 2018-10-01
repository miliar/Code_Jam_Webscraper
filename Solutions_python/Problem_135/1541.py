#!/usr/bin/env python
# -*- coding: utf-8 -*-

T = int(raw_input())

for i in xrange(T):
    r1 = int(raw_input())-1
    a = [0,0,0,0]
    a[0] = set(raw_input().split(" "))
    a[1] = set(raw_input().split(" "))
    a[2] = set(raw_input().split(" "))
    a[3] = set(raw_input().split(" "))
    r2 = int(raw_input())-1
    b = [0,0,0,0]
    b[0] = set(raw_input().split(" "))
    b[1] = set(raw_input().split(" "))
    b[2] = set(raw_input().split(" "))
    b[3] = set(raw_input().split(" "))
    res = a[r1] & b[r2]
    if len(res) == 0:
        ans = "Volunteer cheated!"
    if len(res) == 1:
        ans = list(res)[0]
    if len(res) > 1:
        ans = "Bad magician!"
    print "Case #" + str(i+1) + ": " + ans

