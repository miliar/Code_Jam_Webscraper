import sys, string
import itertools

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

T = int(sys.stdin.readline())

Oppo = {}

def checkoppo(L,e):
	for o in L:
		if Oppo.get((o,e)):
			return 1
	return 0

for t in range(T):
	Comb = {} # combine rules
	Oppo = {} # opposite elements
	L = sys.stdin.readline().strip().split(" ") # num of base elements => third element
	
	C = int(L[0])
	B = L[1:C+1]
	D = int(L[C+1])
	O = L[C+2:C+2+D]
	N = int(L[C+2+D])
	E = L[C+2+D+1]
	#~ print C,B,D,O,N,len(E),E
	
	for b1,b2,r in B:
		Comb[b1,b2] = r
		Comb[b2,b1] = r
	
	for o1,o2 in O:
		Oppo[o1,o2] = 1
		Oppo[o2,o1] = 1
	
	L = []
	#~ print Comb, Oppo
	for e in E:
		#~ print L
		if len(L):
			c = Comb.get((L[-1], e))
			if c:
				L = L[:-1] + [c]
				continue
		
		if checkoppo(L,e):
			L = []
			continue
		
		L.append(e)

	#~ print L
	ans = "[" + string.join(L,", ") + "]"
	print "Case #%d: %s" % (t+1, ans)
