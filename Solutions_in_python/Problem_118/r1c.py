import sys
import math

def IsPalindrome(a):
  c = list('%s' % a)
  for i in range(len(c) / 2):
    if c[i] != c[len(c)-1-i]:
      return False
  return True

def GetPalindromesInRange(a, b):
  n = a
  while True:
    n = GetNextPalindrome(n, smaller=False)
    if n > b:
      return
    yield n
    n = n+1

def GetNextPalindrome(n, smaller=True):
  c = list('%s' % n)
  l = (len(c) + 1) / 2
  sl = (len(c) - 1) / 2
  sr = len(c) / 2
  for i in range(l):
    a = c[sl-i]
    b = c[sr+i]
    if a == b:
      continue
    elif smaller:
      if int(a) < int(b):
        c[sr+i] = a
      else:
        if sl-i == 0 and b == '0':
          return int('9' * (len(c)-1))
        return GetNextPalindrome(n - int(''.join(c[sr+i:])) - 1, smaller=smaller)
    else:
      if int(a) > int(b):
        c[sr+i] = a
      else:
        c[sl-i] = str(int(c[sl-i]) + 1)
        return GetNextPalindrome(int(''.join(c)) - int(''.join(c[sl-i+1:])), smaller=smaller)
  return int(''.join(c))

def ReadCases(inp):
  cases = int(inp.readline())
  for x in range(cases):
    a, b = [int(x) for x in inp.readline().strip().split(' ')]
    yield (a, b)

def TestIsPalindrome(a, exp):
  if IsPalindrome(a) != exp:
    print "Expected IsPalindrome(%s) == %s" % (a, exp)

def TestGetSmallerPalindrome(a, exp):
  s = GetNextPalindrome(a, smaller=True)
  if s > a:
    print "GetSmallerPalindrome: Expected %s <= %s" % (s, a)
  if not IsPalindrome(s):
    print "Expected GetSmallerPalindrome(%s) to be palindrome, got: %s" % (a, s)
  if s != exp:
    print "GetSmallerPalindrome: Expected %s, got %s" % (exp, s)

def TestGetBiggerPalindrome(a, exp):
  s = GetNextPalindrome(a, smaller=False)
  if s < a:
    print "GetBiggerPalindrome: Expected %s >= %s" % (s, a)
  if not IsPalindrome(s):
    print "Expected GetBiggerPalindrome(%s) to be palindrome, got: %s" % (a, s)
  if s != exp:
    print "GetBiggerPalindrome: Expected %s, got %s" % (exp, s)

def Test():
  TestIsPalindrome(131, True)
  TestIsPalindrome(123456789, False)
  TestIsPalindrome(1234567890987654321, True)

  TestGetSmallerPalindrome(1234567890987654321, 1234567890987654321)
  TestGetSmallerPalindrome(1000, 999)
  TestGetSmallerPalindrome(100, 99)
  TestGetSmallerPalindrome(1234, 1221)
  TestGetSmallerPalindrome(4321, 4224)
  TestGetSmallerPalindrome(321, 313)
  TestGetSmallerPalindrome(123, 121)

  TestGetBiggerPalindrome(1000, 1001)
  TestGetBiggerPalindrome(25, 33)

if __name__ == '__main__':
  Test()

  i = 1
  for a, b in ReadCases(sys.stdin):
    sys.stdout.write('Case #%s: ' % i)
    sqrta = int(math.ceil(math.sqrt(a)))
    sqrtb = int(math.floor(math.sqrt(b)))
    n = [x*x for x in GetPalindromesInRange(sqrta, sqrtb) if IsPalindrome(x*x)]
    sys.stdout.write('%s\n' % len(n))
    i += 1
