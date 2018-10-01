#!/usr/bin/env python

def solve():
  c, f, x = map(lambda x: float(x), raw_input().split())
  cookies = 0
  production = 2
  seconds = 0.0

  i = 0
  ans = 999999999999999999999
  while True:
    goal_time = x / production
    next_wait = c / production

    if i > 0:
      goal_time = min(goal_time, (x - c) / (production - f))

    if seconds + goal_time < ans:
      ans = seconds + goal_time
    else:
      return ans

    if goal_time < next_wait:
      return seconds + goal_time
    else:
      seconds = seconds + next_wait
      production = production + f
      i = i + 1

  return seconds

def main():
  n = int(raw_input())
  for i in xrange(n):
    print 'Case #%d: %0.7f' % (i + 1, solve())

if __name__ == '__main__':
  main()
