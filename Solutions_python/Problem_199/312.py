#!/usr/bin/env python

def solve(case_nr):
  answer = 0
  [S, K] = raw_input().split()
  S = [c for c in S]
  K=int(K)
  
  pos = 0
  flips = 0
  while (pos < len(S)):
    if (S[pos] == '-'):
      if ((pos+K-1) < len(S)):
        flips += 1
        for i in xrange(K):
          if S[pos+i] == '-':
            S[pos+i] = '+'
          else:
            S[pos+i] = '-'
        answer = int(flips)
      else:
        answer = 'IMPOSSIBLE'
    pos+=1
  
  print "Case #%d: %s" % (case_nr, answer)


T = int(raw_input())

for i in xrange(T):
  solve(i+1)
