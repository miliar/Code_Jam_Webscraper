#!/usr/bin/env python

T = int(raw_input())

def read_problem():
  c, f, x = [ float(e) for e in raw_input().split() ]
  return c,f,x

def solve(problem):
  c, f, x = problem
  rate = 2.0
  tWin = x / rate
  t = 0
  cookies = 0
  while t + c/rate < tWin:
    t += c/rate
    cookies += c
    tWinNew = t + (x - cookies + c) / (rate + f)
    if tWinNew < tWin: # buy factory
      cookies -= c
      rate += f
      tWin = tWinNew
    else:
      break
  return tWin

for n in range(T):
  problem = read_problem()
  solution = solve(problem)
  print 'Case #%d: %.7f' %(n+1, solution)

