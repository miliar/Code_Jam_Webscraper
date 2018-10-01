def readval(typ=int):
    return typ( raw_input() )

def readvals(typ=int):
    return map( typ, raw_input().split() )

import sys
sys.setrecursionlimit(1000000)
def memoize(f):
    """ Memoization decorator for functions taking one or more arguments.
    to clear the internal DP dict: use f.clear() """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):  
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

from math import pi 
import numpy as np 

def testcase(cas=-1):
    N, K = readvals() 
    RH = sorted([tuple(readvals()) for _ in xrange(N)], reverse=True)
    R, H = zip(*RH)
    
    # @memoize
    # def f(i,k): # returns: max_surface, base_radius
    #     if k<=0: return 0,0 
    #     if N-i < k: return -1e1000, 0 
    #     Sa, Ra = f(i+1, k) 
    #     Sb, Rb = f(i+1, k-1)
    #     Sb = Sb + 2*R[i]*H[i] + R[i]*R[i] - Rb*Rb 
    #     if Sb >= Sa: return Sb, R[i]
    #     else: return Sa, Ra 
    # res = f(0,K)[0] * np.float128(pi)
    @memoize
    def f(i,k): 
        if k <= 0: return 0
        if N-i < k: return -1e100
        return max( f(i+1, k), f(i+1,k-1)+2*R[i]*H[i] )

    res = 0
    for j in xrange(N-K+1): 
        s = R[j]**2 + R[j]*2*H[j] + f(j+1,K-1)
        res = max(s, res) 
    res *= pi 
    print 'Case #%d: %.9f' % ( cas, res )

if __name__=='__main__':
    T = readval()
    for i in xrange(T):
        testcase(i+1)
