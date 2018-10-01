#!/usr/bin/env python3

def process(N):
  s = str(N)
  try:
    f = min(i for i in range(len(s)-1) if s[i+1]<s[i])
  except ValueError:
    return N
  x = s.index(s[f])
  s = s[:x] + chr(ord(s[x])-1) + '9' * (len(s)-x-1)
  return int(s, 10)

T = int(input())
for case in range(1, T+1):
  N = int(input())
  res = process(N)
  print("Case #{}: {}".format(case, res))

