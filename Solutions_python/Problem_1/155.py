import sys
sys.setrecursionlimit(1000000000)

def rint(): return int(sys.stdin.readline())
def rstr(): return sys.stdin.readline()[:-1]

class vertex:
	name = ""
	edges = []
	def __init__(self, astring):
		self.name = astring

mc = {}

def mincost(a):
	if a.edges == []:
		return 0
	elif a in mc:
		return mc[a]
	else:
		try:
			mc[a] = min([mc[e] + (1 if e.name != a.name else 0) for e in a.edges])
		except:
			mc[a] = min([mincost(e) + (1 if e.name != a.name else 0) for e in a.edges])

		return mc[a]
		
def shortest(Y):
	if (len(Y) == 0): return 0

	for i in range(0, len(Y) - 1): # 0..index of second last row
		for v in Y[i]:
			v.edges = [v2 for v2 in Y[i+1]]
	
	return min([mincost(start) for start in Y[0]])

N = rint()

for tc in range(1,N+1):
	s = rint()
	engs = []
	for x in range(0,s):
		engs.append(rstr())
	nq = rint() #num queries

	#print engs

	q = []
	for x in range(0,nq):
		q.append(rstr())
	
	#print q

	Y = []
	for query in q:
		Y.append([vertex(e) for e in engs if e != query])

	#print "<<array Y:>>"
	#for line in Y:
	#	print line
		
	print "Case #" + str(tc) + ": " + str(shortest(Y))
