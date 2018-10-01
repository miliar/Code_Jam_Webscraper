#!/usr/bin/env python3

from collections import Counter
import math

words = ['a', 'b', 'c', 'a']

Counter(words).keys() # equals to list(set(words))
Counter(words).values() # counts the elements' frequency

for L in range(int(input())):
	_,P = map(int, input().split())
	G = map(int, input().split())
	
	G = Counter(g%P for g in G)
	
	out = G[0]
	G[0] = 0
	if P==2:
		out += math.ceil(G[1]/2)
	if P==3:
		while G[2] and G[1]:
			G[1]-=1
			G[2]-=1
			out += 1
		out += math.ceil((G[2]+G[1])/3)
	if P==4:
		while G[3] and G[1]:
			G[1]-=1
			G[3]-=1
			out += 1
		#G3 = 0 or G1 = 0
		while G[2]>=1:
			G[2]-=2
			out += 1
		#(G3=0 or G1=0), G2 = {0,1}
		if G[2]==1 and G[1]>=2:
			G[1]-=2
			G[2]-=1
			out += 1
		out += math.ceil((G[3]+G[2]+G[1])/4)
	
	print("Case #"+str(L+1)+":", out)
