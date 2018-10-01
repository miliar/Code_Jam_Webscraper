import sys
import operator

sys.setrecursionlimit(2000)

def readn(f, n):
	return [f.readline().rstrip('\n') for i in range(n)]

def next(g, pos, k):
	ss = 0
	while True:
		ss+=g[pos]
		if ss > k: return (ss-g[pos], pos)
		pos+=1
		if pos == len(g): pos = 0
	
def solve(R, k, N, g):
	if sum(g) <= k: return R * sum(g)
	hash = {}
	ss = 0
	i = 0
	pos = 0
	while i < R:
		if pos in hash: break
		i+=1
		(nextSum, nextPos) = next(g,pos,k)
		hash[pos]=(nextSum, nextPos)
		ss += nextSum
		pos = nextPos
	R -= i
	if R == 0: return ss
	start = pos
	cLen = 0
	cTot = 0
	while True:
		cLen+=1
		cTot+=hash[pos][0]
		pos=hash[pos][1]
		if pos == start: break
	times = R // cLen
	ss += cTot * times
	
	pos = start
	for j in range(R % cLen):
		ss += hash[pos][0]
		pos = hash[pos][1]
	
	return ss
	
f = open("C-large.in", 'r')

test = int(f.readline())

for tt in range(test):
	(R, k, N) = list(map(int,f.readline().split()))
	g = list(map(int,f.readline().split()))
	
	print("Case #{0}: {1}".format(tt+1, solve(R,k,N,g)))
	
f.close()