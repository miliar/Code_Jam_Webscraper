#!/usr/bin/python
import sys

# C = cost, F = additional freq, X - target
def calc(C, F, X):
  freq = 2.0
  cost = 0
  time_from_curr = X / freq
  best = time_from_curr
  while True:
    time_to_next = C / freq
    if cost > best:
      return best
    time_from_next = X / (freq + F)
    best = min(best, cost + time_to_next + time_from_next)
    cost += time_to_next
    freq += F
    time_from_curr = time_from_next

def main():
  d = file(sys.argv[1]).readlines()
  n = int(d[0])
  for j in xrange(1, n+1):
    C, F, X = map(float, d[j].split())
    print "Case #%d: %.07f" % (j, calc(C, F, X))

main()
