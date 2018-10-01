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

def ints():
    return map(int,raw_input().split())

def main(): drive(solve)

    # '''Test'''
    # @Memoize
    # def fib1(n):
    #     if n <= 1:
    #         return 1
    #     else:
    #         return fib1(n-1) + fib1(n-2)

    # @memoize
    # def fib2(n):
    #     if n <= 1:
    #         return 1
    #     else:
    #         return fib2(n-1) + fib2(n-2)

    # print fib1(1000) == fib2(1000)

def solve(n):
    in_ = ints()
    N = in_[0]
    xs = in_[1:]
    M = max(xs)
    #print M
    #print N,xs


    @memoize
    def search(safe,delta,n):
        #print (safe,delta,n)
        if safe and delta == 0:
            return (True,None,None)
        elif n == N:
            return (False,None,None)
        else:
            d = delta+xs[n]
            if abs(d) <= M:
                (b,ls,rs) = search(True,d,n+1)
                if b:
                    return (True, (xs[n],ls), rs)

            d = delta-xs[n]
            if abs(d) <= M:
                (b,ls,rs) = search(True,delta-xs[n],n+1)
                if b:
                    return (True, ls, (xs[n],rs))

            return search(safe,delta,n+1)

    (b,ls,rs) = search(False,0,0)
    def elems(t):
        if t == None:
            return ""
        else:
            return "%s %s" % (t[0],elems(t[1]))
    if b:
        return "\n%s\n%s" % (elems(ls), elems(rs))
    else:
        return "\nImpossible"

if __name__ == '__main__': main()

