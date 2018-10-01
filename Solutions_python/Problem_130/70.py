#!/usr/bin/env python

def ri():
  x = ''
  while not x:
    x = raw_input().strip()
  return x

def Cost(a,b,p):
  return p*((b-a)*N-(b-a)*(b-a-1)/2)

T = int(ri())
for t in xrange(1,T+1):
  N,P = map(int,ri().split())
  for k in xrange(0,N+1):
    if 2**N-2**k<=P-1: break
  if k==0:
    ans1 = 2**N-1
  else:
    ans1 = 2**(N-k+1)-2
  for k in xrange(N,-1,-1):
    if 2**k <= P:
      break
  ans2 = 2**N-2**(N-k)
  print 'Case #%d:'%t,ans1,ans2
      


