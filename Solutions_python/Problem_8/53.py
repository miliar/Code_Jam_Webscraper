#!/usr/bin/env python

import math, sys

def log( msg ):
    print >>sys.stderr, msg

def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

def solve( a, b, p ):
    rest = range( a, b+1 )

    sets = []
    for t in primes(b):
        if t >= p:
            set = []
            v = t
            while v < a:    v += t
            while v <= b:
                try:
                    rest.remove( v )
                except ValueError:
                    pass
                set.append( v )
                v += t
            if len( set ) > 0:
                sets.append( set )

    i = 0
    while i < len( sets ):
        for n in sets[i]:
            j = i+1
            while j < len( sets ):
                if n in sets[j]:
                    sets[i].extend( [ x for x in sets[j] if x not in sets[i] ] )
                    del sets[j]
                    break
                else:
                    j += 1
        i += 1

    return len( sets ) + len( rest )

N = int( sys.stdin.readline() )
log( "%d test cases" % N )
for i in range( N ):
    A, B, P = [ int(x) for x in sys.stdin.readline().split() ]
    print "Case #%d: %d" % ( i+1, solve( A, B, P ) )
