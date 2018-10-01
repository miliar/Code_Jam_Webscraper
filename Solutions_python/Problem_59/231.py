#!/usr/bin/python
from sys import stdin



TTT = int(stdin.readline())
for ttt in range(1,TTT+1):
  N, M = map(int,stdin.readline().split())
  fs = {}
  for i in range(0, N):
    path = stdin.readline()[:-1].split("/")[1:]
    cur = fs
    for d in path:
      if not cur.has_key(d):
        cur[d] = {}
      cur = cur[d]
  count = 0
  for j in range(0,M):
    path = stdin.readline()[:-1].split("/")[1:]
    cur = fs
    for d in path:
      if not cur.has_key(d):
        cur[d] = {}
        count = count + 1
      cur = cur[d]
  print "Case #%d: %d" % (ttt,count)
