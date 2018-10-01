
import sys

def gcd(a, b):
  while b > 0: a,b = b, a%b
  return a

def biggest_divisor(numbers):
  divisor = abs(numbers[1] - numbers[0])
  m = len(numbers)
  for i in xrange(m):
    for j in xrange(i+1, m):
      divisor = gcd(divisor, abs(numbers[i] - numbers[j]))

  return divisor

def first_to_reach(numbers, divisor):
  m = max(numbers)
  return divisor - m%divisor

t = int(sys.stdin.readline())

for i in xrange(t):
  numbers = map(lambda x: int(x), sys.stdin.readline().split(' ')[1:])
  #print numbers
  divisor = biggest_divisor(numbers)
  x = first_to_reach(numbers, divisor)
  if divisor == x:
    x = 0

  print "Case #%d:" % (1+i), x
  #print divisor
  #print map(lambda y: y+x, numbers)
  #print reduce(lambda x, y: gcd(x, y), map(lambda y: y+x, numbers))
  assert reduce(lambda x, y: gcd(x, y), map(lambda y: y+x, numbers)) == divisor
