#!/usr/bin/python

from sys import stdin

def with_speed(l, running, runtime, walking):
  t = l / running
  t = min(t, runtime)
  runtime -= t

  l_ = l - t * running
  
  if l_:
    t += l_ / walking

  return t, runtime
  

def evaluate_case(length, walking, running, runtime, walkways):
  # Evaluate walkways.
  walkways_ = sorted([(w[2], w[1] - w[0]) for w in walkways])
 
  t = 0
  r = runtime

  w_len = sum(w[1] for w in walkways_)
  t_, r = with_speed(length - w_len, running, r, walking)
  t += t_

  for w in walkways_:
    t_, r = with_speed(w[1], w[0] + running, r, walking + w[0])
    t += t_
    
  return t

def read_list(n):
  walkways = []
  for _ in range(n):
    line = stdin.readline().strip()
    walkways.append(tuple(map(int, line.split())))
  return walkways
  
count = int(stdin.readline())

for i in range(1, count+1):
  length, walking, running, runtime, N = map(int, stdin.readline().split())
  walkways = read_list(N)
  
  t = evaluate_case(length, walking, running, runtime, walkways)
  print('Case #' + str(i) + ': ' + ('%.9f' % t))
