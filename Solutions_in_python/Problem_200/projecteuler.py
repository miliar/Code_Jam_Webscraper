from math import *
from collections import Counter
from time import time
import itertools as it


''' gcd INT A, INT B --> INT C : C is the greatest common divisor of A and B '''
def gcd(a,b): return a if b==0 else gcd(b, a%b)

''' lcm INT A, INT B --> INT C : C is the lowest common multiple of A and B '''
def lcm(a,b): return a*b/gcd(a,b)

''' ofile STRING F --> ARRAY A : A is an array of each line in F, with endlines stripped and split by spacing for convenience '''
def ofile(f): return [l.rstrip().split() for l in open(f).readlines()]

''' finddivisors INT N --> ARRAY A : A is an array of the factors of N, listed in accending order '''
def finddivisors(n): return sorted([i for s in [[i, n/i] for i in xrange(1,int(sqrt(n))+1) if n%i==0] for i in s])

''' factoral INT N --> INT C : C = N! '''
def factorial(n): return 1 if n in [1, 0] else factorial(n-1) * n

''' digitsum INT N --> INT C : C is the sum of the digits in N '''
def digitsum(n): return sum(map(int, [c for c in str(n)]))

''' isprime INT N --> BOOL B : B is true if N is prime '''
def isprime(n): return n in primesieve(n)

''' allequal ARRAY A --> BOOL B : B is true if all elements are equal '''
def allequal(l): return all(e==l[0] for e in l)

''' pandigital ARRAY D, ARRAY N --> BOOL B : B is true if all strings in N contain every character in D '''
def pandigital(digits,numlist):
    nl=''.join([str(i) for i in numlist])+''.join([str(i) for i in digits])
    return all([Counter(nl)[str(c)]==2 for c in digits])

''' countdivisors INT N --> INT C : C is the number of factors an integer N has '''
def countdivisors(n):
    pfs=factorise(n)
    return reduce(lambda x,y:x*y, [pfs.count(c)+1 for c in set(pfs)]) if len(pfs)>1 else 2

''' primesieve INT N --> ARRAY A : A is the set of primes <= N '''
def primesieve(n):
    nums=[False, True] + [i%2==0 for i in xrange(n-1)]
    for i in xrange(3, int(sqrt(n))+1,2):
        if nums[i-1]:
            for j in xrange(i*i, n+1, i):
                nums[j-1]=False
    return set([k+1 for k in xrange(n) if nums[k]])

''' factorise INT N, ARRAY P --> ARRAY A : A is the prime factorisation of N '''
def factorise(n,primes):
    ret=[]
    while n>1:
        for p in primes:
            while n%p==0:
                n/=p
                ret+=[p]
    return ret

''' binsearch ARRAY A, WILD T --> BOOL B : B is true if T exists in A '''
def binsearch(A, target):
    low,high=0,len(A)-1
    mid=(high+low)/2
    while high>=low:
        if target>A[mid]:
            low=mid+1
        elif target<A[mid]:
            high=mid-1
        else:
            return True
        mid=(high+low)/2
    return False

''' rotations INT N --> ARRAY A : A is the set of all numbers formed by moving the first k digits of N to its back for all possible k '''
def rotations(num):
    k=str(num)
    ret=[]
    for i in xrange(len(k)):
        k=k[1:]+k[0]
        ret+=[int(k)]
    return ret

def solution():
    # code solution here (for timing purposes)
    f=open('input.in').readlines()
    t=int(f[0].strip())
    for i in xrange(1,t+1):
        c=int(f[i].strip())
        for m in xrange(c,0,-1):
            if ''.join(sorted(str(m)))==str(m):
                print "Case #%i: %i" % (i, m)
                break
    pass

t=time()
solution()
# print "Took %.4fs" % (time()-t)