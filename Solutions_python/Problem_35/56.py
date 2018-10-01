
import sys
import math
import random

def readstr():
	return sys.stdin.readline().strip()

def readint():
	return int(readstr())

def tolist( stri, delim='' ):
	if delim == '':
		return stri.split()
	else:
		return stri.split( delim )

def readlist( delim='' ): return tolist( readstr(), delim )

def evallist( l, f ):
	v = []
	for i in l:
		v.append( f(i) )
	return v

def readevallist( f, delim='' ):
	return evallist( readlist(delim), f )

def readints( delim='' ): return readevallist( int, delim )

N = readint()

for i in range(N):
	H,W = readints()

	m = []
	for h in xrange(H):
		m += readints()

	comp = []
	for j in range(W*H): comp.append(j)

	c = True
	while c:
		c = False
		for y in xrange(H):
			for x in xrange(W):
				j = y*W + x
				k = comp[j]
				a = m[j]

				pot = []
				if y != 0: pot.append( j - W )
				if x != 0: pot.append( j - 1 )
				if x != W-1: pot.append( j + 1 )
				if y != H-1: pot.append( j + W )

				li = -1
				la = -1

				for p in pot:
					ua = m[p]
					if ua < a:
						if (li == -1 or ua < la):
							li = p
							la = ua
				
				if li != -1:
					uk = comp[li]		
					if uk != k:
						c = True
						comp[j] = uk

	cm = {}
	cur = 0
	for j in xrange(W*H):
		l = comp[j]
		if not l in cm:
			cm[l] = cur
			cur += 1
		comp[j] = cm[l]
	
	print "Case #"+str(i+1)+":"

	for h in xrange(H):
		for w in xrange(W):
			print chr(comp[h*W + w]+ord('a')),
		print ""


