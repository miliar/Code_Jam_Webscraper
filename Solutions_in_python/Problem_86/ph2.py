#!/usr/bin/python
import math
import sys


TC=0
DEBUG=False
if len(sys.argv)>2:
  DEBUG=True
  TC=int(sys.argv[2])

def debugprint(s,t):
  if DEBUG and(t==TC):
    print s


def gcd(a,b):
  c=b
  while (a%b!=0):
    c=a%b
    a=b
    b=c
  return c



input = open (sys.argv[1],'r')
T = int(input.readline())
for t in range(0,T):
  X = map(int,input.readline().rstrip().split(' '))
  N=X[0]
  L=X[1]
  H=X[2]
  O = map(int,input.readline().rstrip().split(' '))
  O.sort()
  for a in range(L,H+1):
    q=True
    for o in O:
      if (a%o!=0 and o%a!=0):
        q=False
        break
    if (q):
      break
  if (q):
    S=a
  else:
    S="NO"
  print "Case #%d: %s" % (t+1,S)

