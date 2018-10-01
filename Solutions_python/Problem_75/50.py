# -*- coding: utf-8 -*-


from collections import defaultdict as dd

T = int(raw_input())

for x in range(1,T+1):
	
	words = raw_input().split()
	
	C = int(words.pop(0))
	comb = {}
	for c in range(C):
		a,b,c = words.pop(0)
		comb[a,b] = comb[b,a] = c
	
	D = int(words.pop(0))
	opps = dd(list)
	for d in range(D):
		a,b = words.pop(0)
		opps[a].append(b)
		opps[b].append(a)
	
	N = int(words.pop(0))
	series = words.pop(0)
	els = []
	for c in series:
		done = False
		if len(els)>=1:
			pair = (els[-1],c)
			if pair in comb:
				els[-1] = comb[pair]	# combine!
				done = True
		if not done:
			opplist = opps[c]
			shouldclear = False
			for o in opplist:
				if o in els:
					shouldclear = True
					break
			if shouldclear:
				els = []
				done = True
		if not done:
			els.append(c)
	
	srep = "[{l}]".format(l=", ".join(els))
	
	print "Case #{x}: {y}".format(x=x,y=srep)

















