'''
Created on Sep 13, 2009

@author: psyho
'''

import operator
import math

def minimum_t(a, b):
    if a[0] == 0 and a[1] == 0 and a[2] == 0: return 0
    numerator = sum(map(operator.mul, a, b))
    denominator = sum(map(operator.mul, a, a))
    t = -1.0*numerator/denominator
    if t < 0: 
        return 0
    else: 
        return t

def distance(t, a, b, n):
    a_sq = sum(map(operator.mul, a, a))
    b_sq = sum(map(operator.mul, b, b))
    ab = sum(map(operator.mul, a, b))
    return math.sqrt(a_sq*t*t + 2*ab*t + b_sq) / n

def main():
    T = int(raw_input())
    for i in xrange(T):
        N = int(raw_input())
        sums = [0.0] * 6
        for n in xrange(N):
            firefly = map(int, raw_input().split())
            for idx in xrange(len(sums)):
                sums[idx] += firefly[idx]
        a = sums[3:]
        b = sums[:3]
        t = minimum_t(a, b)
        dist = distance(t, a, b, N)
        print 'Case #%d: %0.8f %0.8f' % (i+1, dist, t)

if __name__ == '__main__':
    main()
