import math, re, sys

def isPalindrome(number):
  numString = str(number)
  if re.search('\d+\\.0$', numString):
    numString = numString.split('.')[0]
  return numString[:int(math.floor(len(numString)/2.0))] == numString[int(math.ceil(len(numString)/2.0)):][::-1] 

def isFairAndSquare(number):
  return isPalindrome(number) and isPalindrome(math.sqrt(number))

cases = 0
board = []

for count,line in enumerate(sys.stdin):
  if count == 0:
    cases = int(line)
    continue

  A,B = line.strip().split(' ')
  fairCount = 0

  for x in xrange(int(A),int(B)+1):
    if isFairAndSquare(x):
      fairCount += 1

  print "Case #" + str(count) + ": " + str(fairCount)

  if count == cases:
    break
