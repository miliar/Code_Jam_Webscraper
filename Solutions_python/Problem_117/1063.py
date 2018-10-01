# -*- coding: utf-8 -*-

import sys

def readInts():
  line = sys.stdin.readline().rstrip("\n")
  return map(int,line.split(" "))

def solve(N,M,lawn):
  heights = [[100 for m in xrange(M)] for n in xrange(N)]
  for n in xrange(N):
    hmax = lawn[n][0]
    for m in xrange(1,M):
      if lawn[n][m] > hmax:
        hmax = lawn[n][m]
    for m in xrange(M):
      heights[n][m] = min(hmax,heights[n][m])

  for m in xrange(M):
    hmax = lawn[0][m]
    for n in xrange(1,N):
      if lawn[n][m] > hmax:
        hmax = lawn[n][m]
    for n in xrange(N):
      heights[n][m] = min(hmax,heights[n][m])

  for n in xrange(N):
    for m in xrange(M):
      if lawn[n][m] != heights[n][m]:
        return "NO"
  return "YES"
    
if __name__ == "__main__":
  T = readInts()[0]
  for t in xrange(1,T+1):
    N,M = readInts()
    lawn = []
    for n in xrange(N):
      lawn.append(readInts())
    ans = solve(N,M,lawn)
    print "Case #%d: %s"%(t,ans)
