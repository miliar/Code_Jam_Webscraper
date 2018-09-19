import math

def parse_numbers(line):
  return (int(i) for i in line.split())

def is_palindrome(n):
    str_n = str(n)
    if str_n != str_n[::-1]:
      return False
    return True

def get_palindromes(a, b):
  palindromes = []
  for n in xrange(a, b):
    if is_palindrome(n):
      palindromes.append(n)
  return palindromes

def get_sqrts(palindromes):
  fair_square = 0
  for i in palindromes:
    root = math.sqrt(i)
    if not root.is_integer():
      continue
    root = int(root)
    if root % 1 == 0 and is_palindrome(root):
      fair_square += 1
  return fair_square

f = open('C-small-attempt0.in', 'rU')
test_cases = int(f.readline())
for i in xrange(test_cases):
  a, b = parse_numbers(f.readline())
  print "Case #%d: %d" % (i + 1, get_sqrts(get_palindromes(a, b + 1)))
