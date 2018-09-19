

import math

def doProb():

  bucket = buildList()

  f = open('C-large-1.in', 'r')

  numCases = int(f.readline())


  casenum = 0

  lines = f.readlines()
  for line in lines:
    casenum+= 1

    low,high = [int(a) for a in line.split()]
    solve(casenum, low,high, bucket)


def solve(casenum, low,high, bucket):

  """
  count = 0
  for i in range(low, high + 1):
    if i in bucket:
      count+= 1
  """
  res = findNumInRange(bucket, low, high)
  print('Case #' + str(casenum) + ': ' + str(res))

def findNumInRange(bucket, low, high):
  left = findLeft(bucket, low)
  right = findRight(bucket, high)
  return right - left

def buildList(low=1, high=10**14):
  lowr = 1
  highr = 10000000 + 1
  palSquare = []
  for i in range(lowr, highr):
    if isPal(i):
      sqr = i*i
      if isPal(sqr):
        palSquare.append(sqr)
  return palSquare


def isPal(n):
  nStr = str(n)
  return nStr == nStr[::-1]

from bisect import bisect_right, bisect_left

# use with low
def findLeft(bucket, val):
  index = bisect_left(bucket, val)
  return index

# Use with high
def findRight(bucket, val):
  index = bisect_right(bucket, val)
  return index


if __name__ == '__main__':
  doProb()


