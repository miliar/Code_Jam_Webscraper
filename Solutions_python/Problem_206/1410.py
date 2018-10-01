import numpy as np
def printOut(I, p):
  print "Case #{}: {}".format(I, p)

t = int(raw_input())
for I in xrange(1, t + 1):
  D, N = [int(s) for s in raw_input().split(" ")]

  k = []
  s = []
  for i in xrange(0, N):
    k_new, s_new = [int(x) for x in raw_input().split(" ")]
    k.append(k_new)
    s.append(s_new)

  slowest = float(D-k[0])/s[0]
  slowest_i = 0
  for i in xrange(1,N):
    if float(D-k[i])/s[i] > slowest:
      slowest = float(D-k[i])/s[i]
      slowest_i = i

  speed = float(D)/slowest
  printOut(I, speed)