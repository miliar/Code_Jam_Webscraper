#!/usr/bin/python
import sys
T = int(sys.stdin.readline())
for t in range(T):
  v = sys.stdin.readline().split()
  timeO = 0
  timeB = 0
  placeO = 1
  placeB = 1
  N = int(v[0])
  time = 0
  for n in range(1, 2 * N, 2):
    nextPlace = int(v[n+1])
    if v[n] == "B":
      time += 1 + max(0, abs(nextPlace - placeB) - (time - timeB))
      timeB = time
      placeB = nextPlace
    else:
      time += 1 + max(0, abs(nextPlace - placeO) - (time - timeO))
      timeO = time
      placeO = nextPlace
  print "Case #%d: %d" % (t+1, time)