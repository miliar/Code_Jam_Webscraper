r'''
args = ' '.join([
	r'',
])
import os
import sys
#os.system(sys.executable + " %s %s"%(__file__, args))
os.system(r'C:\Python36-32\python' + " %s %s"%(__file__, args))
r'''

# import ctypes
# print(ctypes.cdll.test.test(8))
# raise

input = """\
3
3 1
2 3
2 4
4 4
-1 1 -1
-1 -1 1
-1 -1 -1
1 3
4 1
13 10
1 1000
10 8
5 5
-1 1 -1 -1
-1 -1 1 -1
-1 -1 -1 10
-1 -1 -1 -1
1 4
4 3
30 60
10 1000
12 5
20 1
-1 10 -1 31
10 -1 10 -1
-1 -1 -1 10
15 6 -1 -1
2 4
3 1
3 2
""".splitlines(keepends=True)




import sys
output = sys.stdout
if 1:
	input = open(r'C-small-attempt1.in').readlines()
	input = open(r'C-large.in').readlines()
	output = open("C.out", "w")
	
input = iter(input)

import math
from collections import defaultdict

sys.setrecursionlimit(1500)


def dijkstra(D,H,u):
	print(u)
	
	que = [(u,0.0,H[u][0],H[u][1])]
	#visit = [0] * len(D)
	#visit[u] = 1
	times = [float('inf')]*len(D)
	times[u] = 0
	
	#while 0 in visit:
	visit = [0]*len(D)
	visit[u] = 1
	while 0 in visit:
		n,t,e,s = que.pop()
		print(n)
		times[n] = min(times[n],t)
		visit[n] = 1
		for i,d in enumerate(D[n]):
			if d == -1: continue
			
			if e>=d:
				que += [(i,t + d/s, e-d, s)]
				e1,s1 = H[i]
				que += [(i,t + d/s, e1, s1)]
		que.sort(key=lambda t:t[1], reverse=True)
		#print(que)
		#print(times)
		#print(que)
		#n = min(filter(lambda n:visit[n]==0, range(len(D))), key=lambda n:que[n])
		#visit[n] = 1
		#for i,d in enumerate(D[n]):
		#	if d == -1: continue
		#	que[i] = min(que[i], que[n] + d)
	#print(times)
	return times


def dijkstra(D,H,u):
	visit = [0]*len(D)
	distanse = [float('inf')]*len(D)
	distanse[u] = 0
	#visit[u] = 1
	e,s = H[u]
	while 0 in visit:
		n = min(filter(lambda n:visit[n]==0, range(len(D))), key=lambda n:distanse[n])
		visit[n] = 1
		for i,d in enumerate(D[n]):
			if d == -1: continue
			if distanse[n]+d <= e:
				distanse[i] = min(distanse[i], distanse[n]+d)
	times = [d/s for d in distanse]
	return times
	
def dijkstra2(T,u):
	visit = [0]*len(D)
	times = [float('inf')]*len(D)
	times[u] = 0
	while 0 in visit:
		n = min(filter(lambda n:visit[n]==0, range(len(D))), key=lambda n:times[n])
		visit[n] = 1
		for i,t in enumerate(times):
			times[i] = min(times[i], T[n][i]+times[n])
	
	return times
	
def solve(N,Q,H,D,P):
	#import pdb;pdb.set_trace()
	
	T = [dijkstra(D,H,i) for i in range(len(D))]
	
	
	X = {}
	for u in {u for u,v in P}:
		X[u] = dijkstra2(T,u)
	return [X[u][v] for u,v in P]
	
	

#solve(N,Q,H,D,P)

import time
# raise
caseCnt = int(next(input))
for case in range(1,caseCnt+1):
	N,Q = map(int, next(input).split())
	H = []
	for i in range(N):
		e,s = map(int, next(input).split())
		H += [(e,s)]
	D = []
	for i in range(N):
		*d, = map(int, next(input).split())
		D += [d]
	P = []
	for i in range(Q):
		u,v = map(int, next(input).split())
		P += [(u-1,v-1)]
	t0 = time.time()
	#print((N,Q,H,D,P));sys.stdout.flush()
	res = solve(N,Q,H,D,P)
	print("Case #%d:"%case, *res, file=output)
	print(time.time()-t0)
	sys.stdout.flush()
#'''
