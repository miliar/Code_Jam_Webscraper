#Number Sets

import math

def primes():
    q = 2                    # next candidate for primeness
    D = {}                   # map non-primes to their factors
    while True:              # infinite generator, terminate otherwise
        ps = D.pop(q, None)  # get & remove known factors (if any)
        if ps:               # has some factors -> it's not a prime
            for p in ps:     # move each factor to its next multiple
                D.setdefault(p+q, []).append(p)
        else:                # has no factors -> it's a prime
            D[q*q] = [q]     # mark the only newly-discovered multiple
            yield q          # yield each prime one after the other
        q += 1               # next candidate

def factorise(n):
	global prime, P
	p = 0
	last = -1
	ret = []
	while (n!=1):
		if n%prime[p]==0:
			n = n / prime[p]
			if prime[p]>last:
				last = prime[p]
				if prime[p]>=P: ret.append(prime[p])
		else:
			p+=1
	return ret

for case in range(input()):
	A,B,P = map(int, raw_input().split())
	#gen primes up to B
	prime = []
	for i, p in enumerate(primes()):
		prime.append(p)
		if p>B: break
	
	nsets = B-A+1
	fsets = nsets
	
	fac = []
	#factorise
	for i in range(A,B+1):
		fac.append(factorise(i))
	
	#print fac
	mer = [0] * nsets
	for i in range(nsets):
		for j in range(nsets):
			if i!=j:
				m = 0
				for f in fac[i]:
					if f in fac[j]:
						fac[j].remove(f)
						m = 1
						#if mer[j]==0 and mer[i]==0:
						#	mer[j] = 1
						#	fsets -= 1
						#break
				if m==1:
					fac[i] += fac[j]
					fac[j] = []
					fsets -= 1
					
					
					
	print "Case #%s: %s" % (case+1,fsets)