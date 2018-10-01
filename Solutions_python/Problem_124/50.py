import fileinput
import math
import sys
import scipy.misc
    
def func(layer):
    return 4*layer + 1
def cfunc(layer):
    return 2*layer*layer + 3*layer + 1
def p(l,r,Z):
    #print "p(",l,r,Z,")"
    if l == Z:
        # Swap
        temp = r
        r = l
        l = temp
    if r == Z:
        ans = 0.0
        for i in xrange(l+1):
            ans += scipy.misc.comb(Z-1+i, Z-1)*(0.5**(Z+i))
    else:
        ans =  scipy.misc.comb(l+r, l)*(0.5**(l+r))
    #print "p(",l,r,Z,")",ans
    return ans

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for i in xrange(T):
        N, X, Y = map(int, sys.stdin.readline().split(' '))
        layer = (abs(X)+Y)/2
        #print N, layer, cfunc(layer), func(layer)
        if N > cfunc(layer):
            #print "A"
            ans = 1.0
            print "Case #{}: {}".format(i+1, int(ans))
            continue
        elif N < cfunc(layer-1):
            #print "B"
            ans = 0.0
            print "Case #{}: {}".format(i+1, int(ans))
            continue
        k = N - cfunc(layer-1)
        j = Y+1
        #print "k", k, "j", j
        if k-2*layer >= j:
            #print "C"
            ans = 1.0
            print "Case #{}: {}".format(i+1, int(ans))
            continue
        ans = 0.0
        for a in xrange(j, min(2*layer, k)+1):
            ans += p(k-a, a, 2*layer)

        print "Case #{}: {}".format(i+1, float(ans))
