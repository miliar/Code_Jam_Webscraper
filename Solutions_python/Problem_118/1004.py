'''
Google Code Jam 2013
Qualification Round. Problem C
Author: Jon Eisen

This problem solver uses pycodejam, an open source CodeJam problem runner.
See http://github.com/yanatan16/pycodejam
'''
from codejam import CodeJam, parsers
from itertools import *
from math import sqrt

def iter_memoize(fn):
  '''Memoize a function'''
  from functools import wraps
  memo = {}
  @wraps(fn)
  def memoed_fn(*args):
    try:
      memo[args], ret = tee(memo[args])
      return ret
    except KeyError:
      val = fn(*args)
      memo[args], ret = tee(val)
      return ret
  return memoed_fn

@iter_memoize
def palindromes(digits):
	eff = (digits + 1) / 2
	permutes = map(lambda x: ''.join(imap(str,x)), product(xrange(1,10),*tee(xrange(10),eff-1)))
	return (int(p+''.join(reversed(p[:(len(p)-digits%2)]))) for p in permutes)

def ispal(n):
	s = str(n)
	d = len(s)
	e = (d+1)/2
	f = s[:e]
	return f[:(len(f)-(d%2))] == s[e:]

def get_palindromes(a, b):
	lower = len(str(int(sqrt(a))))
	upper = len(str(int(sqrt(b))))
	x = sqrt(b)
	basis = takewhile(lambda y: y <= x, chain.from_iterable(imap(palindromes, count(lower))))
	squares = (x**2 for x in basis)
	sqbasis = dropwhile(lambda y: y < a, squares)
	return ifilter(ispal, sqbasis)


def solve(ab):
	a, b = ab
	# print a, b, list(get_palindromes(a,b))
	return sum((1 for _ in get_palindromes(a, b)))

if __name__ == "__main__":
	CodeJam(parsers.ints, solve).main()