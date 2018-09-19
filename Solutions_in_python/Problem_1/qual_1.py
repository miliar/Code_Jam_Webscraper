#!/usr/bin/python
import sys

file = sys.argv[1]

def resolve(ses, q, n):
  maxidx = 0
  for se in ses:
    if se not in q:
      return 0
    elif q.index(se) > maxidx:
      maxidx = q.index(se)
  ans = resolve(ses, q[maxidx:], n+1)
  if ans == 0:
    return n+1
  else:
    return ans

def start(file):
  f = open(file)
  N = int(f.readline())
  for i in range(1, N+1):
    S = int(f.readline())
    ses = []
    q = []
    for j in range(0, S):
      ses.append(f.readline()[:-1])
    Q = int(f.readline())
    for k in range(0, Q):
      q.append(f.readline()[:-1])
    ans = resolve(ses, q, 0)
    print 'Case #' + str(i) + ': ' + str(ans)

start(file)
