import sys, timeit

sys.setrecursionlimit(sys.maxint)

class Memoize(object):
    def __init__(self, f):
        self.cache = {}
        self.f = f
    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.f(*args)
        return self.cache[args]
    def reset(self):
        self.cache = {}

def memoize(f):
    cache = {}
    def g(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return g

def drive(f):
    N = input()
    for n in range(1,N+1):
        print 'Case #%i:' % n, f(n)

def main():
    '''Test'''
    @Memoize
    def fib1(n):
        if n <= 1:
            return 1
        else:
            return fib1(n-1) + fib1(n-2)

    @memoize
    def fib2(n):
        if n <= 1:
            return 1
        else:
            return fib2(n-1) + fib2(n-2)

    print fib1(1000) == fib2(1000)

if __name__ == '__main__': main()
