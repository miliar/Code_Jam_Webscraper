from functools import *
import math

def end(t,c):
  print('Case #' + str(t) + ': ', end='')
  print(str(c))

def fns(x):
  return isPal(x) and isPal(root(x))

def inv_fns(x):
  return isPal(x) and isPal(x**2)

def isPal(x):
  x = str(x)
  return min([a == b for a,b in zip(x,reversed(x))])

def root(x):
  lz = x ** 0.5
  lz = round (lz)
  if (lz ** 2 == x):
    return lz
  else:
    return 10

testcases = int(input())
memo = [x for x in range(1,10000000) if inv_fns(x)]
#memo = [x for x in range(1,1000) if inv_fns(x)]

for tc in range(1, testcases + 1):
  A,B = [int(x) for x in input().split()]
  # Naive solution
  #count = sum([int(fns(x)) for x in range(A,B+1)])

  # Better solution
  A = math.ceil(A ** 0.5)
  B = math.floor(B ** 0.5)
  count = 0
  for x in memo:
    if A <= x and B>= x:
      count = count + 1

  end(tc,count)
