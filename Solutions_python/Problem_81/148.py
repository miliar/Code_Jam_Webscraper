import operator
import itertools
import sys
from sys import stdin

def solve(tab, size):
  sums = []

  for i in range(0, size):
    total = 0
    num = 0
    for j in range(0, size):
      if tab[i][j] != None:
        total += 1
        num += tab[i][j]
    sums.append((1.*total, num))
    

  OWP = []
  for i in range(0, size):
    acc = 0.
    num = 0.

    for j in range(0, size):
      if j == i:
        continue

      if tab[j][i] == None:
        continue
        #acc += sums[j][1] / sums[j][0]
      else:
        num += 1.
        acc += (sums[j][1] - tab[j][i])/(sums[j][0] - 1.)

    OWP.append(acc/(num))


  OOWP = []
  for i in range(0, size):
    acc = 0.
    num = 0.

    for j in range(0, size):
      if tab[j][i] == None:
        continue
      else:
        acc += OWP[j]
        num += 1.

    OOWP.append(acc/num)

  res = []
  for i in range(0, size):
    res.append(0.25 * sums[i][1]/sums[i][0] + 0.5 * OWP[i] + 0.25 * OOWP[i])

  return res
  
f = stdin
#f = open('a.in')
cases = int(f.readline())
for i in xrange(0, cases):
  size = int(f.readline())
  tab = []
  for j in range(0, size):
    tmp = []
    for c in f.readline().rstrip():
      if c == '.':
        tmp.append(None)
      else:
        tmp.append(float(c))
    tab.append(tmp)

  res = 0
  res = solve(tab, size)
  print 'Case #%d:' % (i+1)

  for val in res:
    print val
