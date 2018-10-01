#!/usr/bin/python

import sys

def solve(n,m):
  done = []
  need = []
  cnt = 0
  for i in range(n):
    done.append( sys.stdin.readline().strip() )
  for i in range(m):
    need.append( sys.stdin.readline().strip() )
  for p in done:
    pp = p.split('/')
    for i in range(2,len(pp)+1):
      np = '/'.join(pp[0:i])
      if (not np in done):
        done.append( '/'.join(pp[0:i]) )
  for p in need:
    pp = p.split('/')
    for i in range(2,len(pp)+1):
      np = '/'.join(pp[0:i])
      if (not np in done):
        cnt += 1
        done.append(np)
  return cnt

t = int(sys.stdin.readline())

for i in range(1,t+1):
  x = map(int, sys.stdin.readline().strip().split(' '))
  print 'Case #%d:' % i, solve(x[0],x[1])
