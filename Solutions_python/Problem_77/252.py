import sys
import math

T = int(sys.stdin.readline())

def good(n):
    if n == 0:
        return 0
    elif n == 2:
        return 2
    else:
        return 1./(1./n*(1.+.5*(n-1.))) + (good(n-1)*3)/4.

def num(n):
    return math.factorial(n-1)*(1+(n-1)/2.)

for _t in xrange(T):

    N = int(sys.stdin.readline())
    array = [int(x) for x in sys.stdin.readline().split()]

    count = 0
    i = 0
    while i < N:
        if array[i] != sorted(array)[i]:
            count += 1
        i += 1

    print "Case #%d: %.6f" % (_t+1, count)

