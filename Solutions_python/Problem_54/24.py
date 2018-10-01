#! /usr/bin/env python
import sys, re
# some reading functions
getline = lambda f: f.readline().strip()
gettoken = lambda f: re.split("\s+", getline(f))
getint = lambda f: int(getline(f))
getints = lambda f: map(int, gettoken(f))

# number theory / combinatorics
product = lambda l: reduce(lambda x,y: x*y, l) if l else 1
factorial = lambda n: product(xrange(n, 1, -1))
nPr = lambda n, r: product(xrange(n,n-r,-1))
nCr = lambda n, r: nPr(n, r) / factorial(r)
nMr = lambda l: factorial(sum(l)) / product(map(factorial,l))
lcm = lambda x,y: x * y / gcd(x, y)
def gcd2(a, b):
    if b == 0: return (a, 1, 0)
    (d,x,y) = gcd2(b, a % b)
    return (d, y, x - a / b * y)
def gcd(x, y): return x if y == 0 else gcd(y, x % y)

def egcd(x, y):
    if y == 0: return (x, 1, 0)
    (d, a, b) = egcd(y, x % y)
    return (d, b, a - x / y * b)

def crt(a, m, b, n):
    (d, u, v) = egcd(m, n)
    if d != 1: return -1
    d, M = u*m*b + v*n*a, m*n
    return (d % M, M)

def main():
    print egcd(13, 5)
    print egcd(27, 12)

def modinv(n, p):
    (d, a, b) = egcd(n, p) #na + pb = 1
    return a % p


if __name__ == "__main__":
    f = open(sys.argv[1]) # open file

    [N] = getints(f)
    for cases in xrange(0,N): # loop over cases
        ans = 0
        # main

        t = getints(f)[1:]
        l = []
        for i, a in enumerate(t):
            for j, b in enumerate(t):
                if j >= i: break
                l.append(abs(a - b))
        T = reduce(gcd, l)
        ans = (T - t[0]) % T
            
        
        # main
        print "Case #%d: %d"%( cases+1, ans ) # answer output
