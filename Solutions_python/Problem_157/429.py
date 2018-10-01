import sys
import random
import itertools


class Quaternion:
    def __init__(self, sign, c):
        self.sign = sign    # +1 or -1
        self.c = c          # '1', 'i', 'j' or 'k'
    
    def __neg__(self):
        return Quaternion(-self.sign, self.c)
    
    def __mul__(self, other):
        sign = self.sign * other.sign
        if self.c == '1':
            return Quaternion(sign, other.c)
        elif other.c == '1':
            return Quaternion(sign, self.c)
        elif self.c == other.c:
            return Quaternion(-sign, '1')
        elif self.c == 'i' and other.c == 'j':
            return Quaternion(sign, 'k')
        elif self.c == 'j' and other.c == 'k':
            return Quaternion(sign, 'i')
        elif self.c == 'k' and other.c == 'i':
            return Quaternion(sign, 'j')
        else:
            return -(other*self)
    
    def __pow__(self, n):
        if n == 0:
            return Quaternion(1, '1')
        
        elif n % 2 == 0:
            a = self**(n/2)
            return a*a
        
        else:
            return self*(self**(n-1))
    
    def __eq__(self, other):
        return self.sign == other.sign and self.c == other.c
    
    def __ne__(self, other):
        return not (self == other)
    
    def __unicode__(self):
        if self.sign == 1:
            return u'%s' % self.c
        else:
            return u'-%s' % self.c
    
    def __repr__(self):
        return self.__unicode__()



def product(l):
    res = Quaternion(1,'1')
    for q in l:
        res = res * q
    return res

def solve():
    i = Quaternion(1, 'i')
    j = Quaternion(1, 'j')
    k = i*j
    
    l, x = [int(x) for x in sys.stdin.readline().split()]
    # print l, x
    quaternions = [Quaternion(1, c) for c in sys.stdin.readline().replace('\n','')]
    # print quaternions
    
    if product(quaternions) ** x != Quaternion(-1, '1'):
        return False
    
    powers = [product(quaternions)**n for n in xrange(4)]
    
    prefixes = []
    aggregate = Quaternion(1,'1')
    for q in quaternions:
        prefixes.append(aggregate)
        aggregate = aggregate * q
    
    first_i = None
    idx = 0
    for (p, pref) in itertools.product(powers, prefixes):
        if p*pref == i:
            first_i = idx
            break
            
        idx += 1
    
    suffixes = []
    aggregate = Quaternion(1,'1')
    for q in reversed(quaternions):
        suffixes.append(aggregate)
        aggregate = q * aggregate
    
    first_k = None
    idx = 0
    for (p, suff) in itertools.product(powers, suffixes):
        if suff*p == k:
            first_k = idx
            break
        
        idx += 1
    
    if first_i is None or first_k is None:
        return False
    
    return first_i + first_k <= l*x


t = int(sys.stdin.readline())
for i in xrange(t):
    print "Case #%d:" % (i+1),
    if solve():
        print 'YES'
    else:
        print 'NO'



