from sys import *
from sets import Set

def solution(case, A, B):
  sum = 0
  for n in xrange(A, B+1):
    nodup = Set()
    for m in xrange(n+1, B+1):
      n = str(n)
      for t in xrange(1, len(n)):
        if (int(n[t:] + n[0:t]) == m):
          nodup.add((n, m))
    sum += len(nodup)
    
  print "Case #%d: %d" % (case+1, sum)
  
T = int(raw_input())
for case in xrange(T):
  L = map(int, stdin.readline().split())
  solution(case, L[0], L[1])