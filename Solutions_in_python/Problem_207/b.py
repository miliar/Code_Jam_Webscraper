from itertools import permutations
import sys
from fractions import gcd
import functools

class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)


def f(fa,fb,fc):
    if max(fa) == 1:
        return '',fa
    else:
        fa[fc] -= 1
        fd = fa[0:fc] + [-1] + fa[fc+1:]
        fd = fd.index(max(fd))
        return  fb[fc] + f(fa,fb,fd)[0], f(fa,fb,fd)[1]

sys.setrecursionlimit(10000)
for i in range(1, 1+input()):
    ca = map(int, raw_input().split())
    ca = ca[1:]
    cb = ['R','O','Y','G','B','V']
    ci = ca.index(max(ca))

    cc, cd = f(ca, cb, ci)
    ce = ''
    for ci, cj in enumerate(cd):
        if cj == 1:
            ce += cb[ci]

    ce = permutations(ce)
    for ci in ce:
        ci = ''.join(ci)
        if cc == '':
            cz = ci
            break
        if ci[0] != cc[-1] and ci[-1] != cc[0]:
            cz = cc + ci
            break
    else:
        cz = 'IMPOSSIBLE'

    print "Case #{}: {}".format(i, cz)

    
    


