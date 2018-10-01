import sys, math
from math import *

D = {}
q = 3
def sieve():
    global D, q
    while True:
        p = D.pop(q, 0)
        if p:
            x = q + p
            while x in D: x += p
            D[x] = p
        else:
            yield q
            D[q*q] = 2*q
        q += 2

def binsearch( n, l, start, end ):
    if end-start <= 1:
        return start
    i = (end+start)/2
    if l[i] <= i:
        if i+1 == end or l[i+1] > i:
            return i
    if l[i] > n:
        return binsearch( n, l, start, i)
    else:
        return binsearch( n, l, i, end )

primes = [2]

def solvecase(n):
    if n == 1:
        return 0
    if n > primes[-1]:
        for i in sieve():
            if i > n:
                break
            primes.append(i)

    indx = binsearch( n, primes, 0, len(primes) )
    f = 0
    for i in range(indx+1):
        k = primes[i]
        while k <= n:
            f += 1
            k *= primes[i]
        
    return f-indx

def parsecase():
  n = int( sys.stdin.readline().strip() )
  return solvecase(n)

def parsecases():
  t = sys.stdin.readline().strip()
  t = int(t)
  return t

def main():
  cases = parsecases()
  i = 1
  while i <= cases:
    print "Case #%s: %s" % (i, parsecase() )
    i += 1

if __name__ == "__main__":
    main()
