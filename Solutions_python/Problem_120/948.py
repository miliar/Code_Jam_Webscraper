import string
import array
import copy
import math


def maxrings(r, t):
  n = 0
  while t >= 0:
    mlforring = 2*r + 1 # area of circle inner radius r, outer radius r+1
    #print "mlforring = %f" % (mlforring)
    t = t - mlforring
    #print "t = %f" % (t)
    n = n + 1
    r = r + 2
  return n - 1
  

f = open('problem1', 'r')
results = []
ncases = int(f.readline())
while ncases > 0:
  [r, t] = f.readline().strip().split(' ')
  print "r=%s, t=%s" % (r,t)
  result = maxrings(int(r), int(t))
  print result
  results.append('Case #%s: %s' % (len(results)+1, result))
  ncases = ncases - 1

for result in results:
  print result