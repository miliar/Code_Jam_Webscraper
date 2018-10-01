import sys
import math

tests_count = int(sys.stdin.readline())


mul_d = {'1' : 0, 'i' : 1, 'j' : 2, 'k' : 3}

mul_t =[[(1,'1'),( 1,'i'),( 1,'j'),( 1,'k')],
		[(1,'i'),(-1,'1'),( 1,'k'),(-1,'j')],
		[(1,'j'),(-1,'k'),(-1,'1'),( 1,'i')],
		[(1,'k'),( 1,'j'),(-1,'i'),(-1,'1')]]


def mult (a,b):
	t = mul_t [ mul_d[a[1]] ] [ mul_d[b] ]
	return (t[0] * a[0], t[1]) 

def check(s,L):
	muli = (1,'1')
	l = len(s)
	for i,c in enumerate(s):

		if i > 4*L :
			break
		muli = mult(muli, s[i])
		if muli[1] != 'i' or muli[0] != 1:
			continue
		mulj = (1,'1')
		for j in xrange(i+1,l):
			if j - i > 4*L :
				break
			mulj = mult(mulj, s[j])
			if mulj[1] != 'j' or mulj[0] != 1:
				continue
			mulk = (1,'1')
			for k in xrange(j+1,l):
				mulk = mult(mulk, s[k])
			if mulk[1] != 'k' or mulk[0] != 1:
				return "NO"

			#print i,j,k
			#print s[:i+1]
			#print s[i+1:j+1]
			#print s[j+1:k+1]
				
			return "YES"
				

	return "NO"

for k in xrange(tests_count):
	
	L,K= map(int, sys.stdin.readline().split(" "))
	s = sys.stdin.readline()[:-1] * K
			
	print "Case #{}: {}".format(k + 1, check(s,L))