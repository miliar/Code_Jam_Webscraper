from sys import stdin as fp
import math
from fractions import gcd

def possible_fraction(P, Q):
    num = math.log(Q / gcd(P, Q), 2)
    if num == int(num):
        return True
    return False
        


def solve(P, Q, n):
    # print P, Q, n
    if n >= 40 or not possible_fraction(P, Q):
        return "impossible"
    if 2*P - Q >= 0 and  possible_fraction(2*P - Q, Q):
        return n + 1
        
    return solve(2*P, Q, n + 1)
    

T = int(fp.readline())
for i in xrange(T):
    P, Q = map(int, fp.readline().split('/'))
    print "Case #%s: %s" % (i+1, solve(P, Q, 0))    
