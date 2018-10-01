from math import pi
from functools import lru_cache
t=int(input())
@lru_cache(1<<32)
def valor(i,k,rmax):
	if i<0 or k<=0: return pi*rmax**2
	if i>=len(pancakes): return pi*rmax**2
	return max(2*pi*pancakes[i][0]*pancakes[i][1]+valor(i+1,k-1,max(rmax,pancakes[i][0])),valor(i+1,k,rmax))
for k in range(t):
	valor.cache_clear()
	global pancakes
	pancakes=[]
	s=0
	N,K=map(int,input().split())
	for i in range(N):
		Ri,Hi=map(int,input().split())
		pancakes.append((Ri,Hi,2*pi*Ri*Hi))
	print("Case #{:.0f}: {:.9f}".format(k+1, valor(0,K,0)))
