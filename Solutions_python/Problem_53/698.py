#!/usr/bin/python

import sys, os

"""
0 0 0 0

1 0 0 0
0 1 0 0
1 1 0 0
0 0 1 0
1 0 1 0
0 1 1 0
1 1 1 0

0 0 0 1

1 0 0 1
0 1 0 1
1 1 0 1
0 0 1 1
1 0 1 1
0 1 1 1
1 1 1 1 (15)

0 0 0 0  (16)

another 15 for next 1, so next on is at 31

(47 / 15 - 1) - (47 % 15) == 0 

k = m + (k-m)/(m+1)

(k-m) % (m+1) == 0

79

(79 - 15) % (15+1) = 0
"""

def calculateMinSnaps(n):

  if n == 1:
    return 1

  return (2*calculateMinSnaps(n-1) + 1)
#calculateMinSnaps

def evalSnapper(n, k):
  if n < 1 or k <= 0:
    return False

  if n == 1:
    if k % 2:
      return True
    else:
      return False
  
  divisor = calculateMinSnaps(n)

  #print "Num snaps for turning on light for %d snappers = %d" %(n, divisor)
  if k < divisor:
    return False

  if k == divisor:
    return True

  #if ( (k/divisor - 1) == (k%divisor)):
  if ( (k - divisor) % (divisor + 1)) == 0:
    return True

  return False
   

# evalSnapper

def main():

  inputFile = open(sys.argv[1], 'r');

  count = 0
  case = 0
  for line in inputFile:

    line = line.strip()
    if not count:
      count = int(line)
      case = case + 1
      continue

    
    splitLine = line.split()
    n = int(splitLine[0])
    k = int(splitLine[1])

    isOn = "OFF" 
    if evalSnapper(n, k):
      isOn = "ON"
    
    print "Case #%d: %s" %(case, isOn)
    case = case + 1

#main

if __name__ == "__main__":
  main()
