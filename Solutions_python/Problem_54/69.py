#!/usr/bin/python

import sys

def gcd(x,y):
  while y>0: x,y = y,x%y
  return x

def abs(x):
  if (x > 0):
    return x
  return -x

T = int(sys.stdin.readline())

for t in range(T):
  d = map(int, sys.stdin.readline().split() )
  d = d[1:]

  G = abs(d[1] - d[0])

  for i in range(len(d)):
	for j in range(i):
		G = gcd(G, abs(d[i] - d[j]))
#  for i in range(1, len(d)):
#	G = gcd(G, abs(d[i] - d[0]))


  y = 0
  if (G != 1): 
     for i in range(len(d)):
	x = (int)(d[i] / G)
	if (-d[i] + G * x < 0): x += 1
	y = max(y, -d[i] + G * x)
	

  print ("Case #%d: %d") % (t + 1, y)
