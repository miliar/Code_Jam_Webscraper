import sys
import math

inputFile = sys.stdin
count = int(inputFile.readline())

class memoize:
  def __init__(self, function):
    self.function = function
    self.memoized = {}

  def __call__(self, *args):
    try:
      return self.memoized[args]
    except KeyError:
      self.memoized[args] = self.function(*args)
      return self.memoized[args]

@memoize
def factorial(n) :
  if n <= 0 : return 1
  return math.factorial(n)

def choose(n, r) :
    return factorial(n) / (factorial(r)  * factorial(n - r))

def choose(n, k):
  if 0 <= k <= n:
    p = 1
    for t in xrange(min(k, n - k)):
      p = (p * (n - t)) // (t + 1)
    return p
  else:
    return 0

@memoize
def pure(n):
  print n
  if n == 1: return 'blarg'
  if n == 2: return [1]

  ret = [0]*(n-1)
  ret[0] = 1 #starts in the 1th position
  for i in xrange(2, n):
    p = pure(i)

    distance = n - i

    for j in xrange(len(p)):
      position = j + 1
      count = p[j]
      
      desired_position = i

      # to get into the i, position i have to be `distance` away
      space = desired_position - position

      ways = choose(distance-1, space-1)
    
      # print "##"
      # print n, i, position, desired_position, space, ways
      if distance < space:
        continue
      ret[desired_position - 1] += count * ways
  return ret

for lineno in xrange(1, count+1):
  n, = map(int, inputFile.readline().split())
 
  # print n, pure(n)
  num = sum(pure(n))
  print "Case #%d:" % lineno, 
  print num % 100003
  sys.stdout.flush()

  lineno += 1
