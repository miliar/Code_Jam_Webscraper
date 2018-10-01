#!/usr/bin/python

from sys import stdin

def shift(seq, n):
  return seq[n:]+seq[:n]

T = int(stdin.readline())
for i in range(1, T+1):
  line = stdin.readline().split()
  A, B = (int(x) for x in line)
  
  pairs = dict()
  for n in range(A, B + 1):
    for j in range(len(str(n))):
      m = shift(str(n), j + 1)
      
      if int(m) <= B and int(m) > n and m >= A:
        pairs[int(n), int(m)] = True
  
  
  print "Case #{}: {}".format(i, len(pairs.keys()))