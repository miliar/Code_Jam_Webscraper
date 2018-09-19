def item_index(L, x):	
	try: r = L.index(x)+1
	except: r = False
	#print x, L, r
	return r

def ispure(k, L ):
	n = len(L)
	k1 = item_index(L, k)
	#print k1
	while k1 > 1: 
		k2 = item_index(L, k1)
		if k2>k1: return False
		k1 = k2
	return k1 == 1

def compute(n):
	a = range(2, n+1)
	r = 0
	for k in xrange(1, n):
		for c in itertools.combinations(a, k):
			if ispure(n, c):
				r+=1
	return r
	
import itertools, sys

n = int(sys.argv[1])

for i in xrange(2, n+1):
	print i, compute(i)