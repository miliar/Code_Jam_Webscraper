import sys
from operator import mul

x = sys.stdin.read().split('\n')
count = x[0]


def rightaway(A, B, l):
    return 2 + B

def keep(A, B, l):
    right = reduce(mul, l)
    wrong = 1 - right
    return (B-A +1 )*right + (2+(B-A)+ B)*wrong


def escape(A, B, l):
    expected = 0
    m = float("inf")
    for i in range(1,A):
        expected = 0
        right = reduce(mul, l[:0-i])
        #print "i=%d, right=%.2f" % (i,right)
        expected += right * ((B - A + i) + i +  1)
        expected += (1 - right) * ((B-A+i)+i+1 + B +1)
        #print "expected=%.2f" % (expected)
        if expected < m:
            m = expected
    everything = A + A +B+ 1
    if everything < m:
        m = everything
    return m





i = 1
counter = 1
while i < len(x)-1:
    A, B = map(int, x[i].split())
    l = map(float, x[i+1].split())
    mult = reduce(mul, l)
    print "Case #%d: %.6f" % (counter, min(rightaway(A,B,l ), keep(A,B,l), escape(A,B,l)))
    #print
    #print
    #print rightaway(A,B,l )
    #print keep(A,B,l)
    #print (escape(A,B,l))
    #print
    #print
    i = i+2
    counter += 1
