import time
import os
import sys
import itertools
import functools
import math

# ----------------------------------------------------------------------

def is_equal_approx(x, y, epsilon=1e-6):
    """ Returns True iff y is within relative or absolute 'epsilon' of x.
        By default, 'epsilon' is 1e-6.
    """
    # Check absolute precision.
    if -epsilon <= x - y <= epsilon:
        return True

    # Is x or y too close to zero?
    if -epsilon <= x <= epsilon or -epsilon <= y <= epsilon:
        return False

    # Check relative precision.
    return (-epsilon <= (x - y) / x <= epsilon
        or -epsilon <= (x - y) / y <= epsilon)
  
def read_syms(fd):
    return [c for c in fd.readline().strip()]

def read_ints(fd):
    return [int(p) for p in fd.readline().strip().split()]

def read_floats(fd):
    return [float(p) for p in fd.readline().strip().split()]

class memoizeit(object):
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
            return self.func(*args)
    
    @property
    def __name__(self):
        return self.func.__name__
    
    def __get__(self, obj, objtype):
        return functools.partial(self.__call__, obj)

class timeit(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        start = time.time()
        value = self.func(*args)
        delta = time.time() - start
        print self.func.__name__, "{:7.3f}s, (res: {})".format(delta, value)
        return value
    def __get__(self, obj, objtype):
        return functools.partial(self.__call__, obj)

# ----------------------------------------------------------------------
