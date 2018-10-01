import os
import sys
import numpy as np

fname = sys.argv[1]

f = open(fname)
lines = f.readlines()
lines = [x.rstrip() for x in lines]
cases = int(lines[0])
for i in range(0, cases):
  n, m = lines[i+1].split(' ')
  n = int(n)
  arr = [m[j] for j in range(0, n+1)]
  arr = [int(x) for x in arr]
  arr = np.array(arr)
  arr2 = np.cumsum(arr)

  ones = np.ones(n+1)
  sums = np.cumsum(ones)
  maximum = int(-min(arr2-sums))
  if maximum < 0:
    maximum = 0

  print "Case #{}: {}".format(i+1, maximum)

