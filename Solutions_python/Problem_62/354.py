#! /usr/bin/env python
#coding=utf-8
import sys, os
f = open('A-small-attempt1.in', 'r')
out = open('a.out', 'w')
sys.stdout = out
sys.stdin = f
input = sys.stdin.readline
t = int(input())

for i in xrange(t):
    s = input().split()
    n = map(int, s)
    count = 0
    print "Case #%d:" % (i+1),
    a = []
    b = []
    for j in xrange(n[0]):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ab = dict(zip(a,b))
    a.sort()
    m = a[0]-ab[a[0]]
    index = 0
    for j in xrange(1, len(a)):
        if ab[a[j]] >= ab[a[index]]:
            m = abs(a[j]-ab[a[j]])
            index = j
            continue
        else:
            if a[j]-ab[a[j]] > m:
                count =count + 1
    print count

f.close()
out.close()
