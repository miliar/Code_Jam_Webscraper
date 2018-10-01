from re import *
from sys import stderr
def readint():
    return int(raw_input())
def readfloat():
    return float(raw_input())
def readarray(N, foo=raw_input):
    return [foo() for i in xrange(N)]
def readlinearray(foo=int):
    return map(foo, raw_input().split())

def NOD(a, b):
    while b:
        a,b = b, a%b
    return a

def gen_primes(max):
    primes = [1]*(max+1)
    for i in range(2, max+1):
        if primes[i]:
            for j in range(i+i, max+1, i):
                primes[j] = 0
    primes[0] = 0
    return [x for x in range(max+1) if primes[x]]

def is_prime(N):
    i = 3
    if not(N % 2):
        return 0
    while i*i < N:
        if not(N % i):
            return 0
        i += 3
    return 1

def dist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def test(XY, r):
    for i in xrange(len(r)):
        for j in xrange(i):
            if dist(XY[i], XY[j]) < (r[i]+r[j])**2:
                return False
    return True

from random import randrange
case_number = readint()
for case in xrange(case_number):
    N, W, L = readlinearray()
    r = readlinearray()
    XY = [() for i in xrange(N)]
    while True:
        for i in xrange(N):
            XY[i] = (randrange(W), randrange(L))
        if test(XY, r):
            break
    print "Case #%s: %s" % (case + 1, ' '.join(map(lambda p: '%d %d' % (p[0], p[1]), XY)))

