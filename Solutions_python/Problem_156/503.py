# Qualification Round 2015
# Problem B. Infinite House of Pancakes
# MichelJ

import sys
import logging
import StringIO
from itertools import chain

def echo(fn):
    def wrapped(*v, **k):
        name = fn.__name__
        logging.info( "Called %s(%s)" % (name, ", ".join(map(repr, chain(v, k.values())))) )
        res = fn(*v, **k)
        logging.info( "       %s(%s) returned %s" % (name, ", ".join(map(repr, chain(v, k.values()))),res) )
        return res
    return wrapped

class memoized(object):
   """Decorator that caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned, and
   not re-evaluated.
   """
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      try:
         return self.cache[args]
      except KeyError:
         value = self.func(*args)
         self.cache[args] = value
         return value
      except TypeError:
         # uncachable -- for instance, passing a list as an argument.
         # Better to not cache than to blow up entirely.
         return self.func(*args)
   def __repr__(self):
      """Return the function's docstring."""
      return self.func.__doc__
   def __get__(self, obj, objtype):
      """Support instance methods."""
      return functools.partial(self.__call__, obj)

def solve(d, p):
    step = 0
    p.sort(reverse=True)
    while True:
#        print p
        if len(p) == 0:
            return repr(step)
        pmax = p[0]
        redist = pmax // 2
        gain = pmax - redist
        nmax = p.count(pmax)
        if gain > nmax:
            p[0] = pmax - redist
            p.append(redist)
            p.sort(reverse=True)
        else:
            p = [pi - 1 for pi in p if pi > 1]
        step += 1

def solve2(d, p):
    return cost(tuple(sorted(p, reverse=True)))

@memoized
def cost(p):
#    print p
    if len(p) == 0:
        return 0
    p1 = [pi - 1 for pi in p if pi > 1]
    pmax = p[0]
    redist = pmax // 2
    nmax = p.count(pmax)
    if redist > 0:
        mincost = 1000000
        pt = list(p)
        for r in xrange(1, redist+1):
            p2 = [pmax - r] + pt[1:] + [r]
            p2.sort(reverse=True)
            costp2 = cost(tuple(p2))
            if costp2 < mincost:
                mincost = costp2
        return 1 + min(cost(tuple(p1)), mincost)
    return 1 + cost(tuple(p1))

    
def main(data=None):
    if data is not None:
        sys.stdin = StringIO.StringIO(data)
    for tc in xrange(1, int(raw_input()) + 1):
        d = int(raw_input())
        p = map(int, raw_input().split(' '))
        print 'Case #%d: %s' % (tc, solve2(d, p))
    if data is not None:
        sys.stdin = sys.__stdin__

sample="""3
1
3
4
1 2 1 2
1
4
"""


# Call main() only if run from command line, not from IDLE
if __name__ == "__main__":
    if True:
#    if '/' not in sys.argv[0] and '\\' not in sys.argv[0]:
        logging.basicConfig(level=logging.ERROR)
        sys.exit(main())
    else:
        logging.basicConfig(level=logging.INFO,format=" %(levelname)s: %(message)s")
