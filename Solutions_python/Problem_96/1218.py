#!/usr/bin/python

from sys import stdin

T = int(stdin.readline())
for i in range(1, T+1):
  line = stdin.readline().split()
  
  N = int(line[0])
  S = int(line[1])
  p = int(line[2])
  
  scores = []
  for j in range(1, N+1):
    scores.append(int(line[2 + j]))
  
  maximum = 0
  for x in scores:
    if x % 3 == 0 and x // 3 >= p:
      maximum += 1
    elif x % 3 > 0 and x // 3 >= p - 1:
      maximum += 1
    elif x % 3 == 0 and x // 3 >= p - 1 and S > 0 and x >= 2:
      maximum += 1
      S -= 1
    elif x % 3 == 2 and x // 3 >= p -2 and S > 0 and x >= 2:
      maximum += 1
      S -= 1
  
  print "Case #{}: {}".format(i, maximum)
      