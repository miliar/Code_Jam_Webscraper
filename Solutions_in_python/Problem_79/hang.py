#! /usr/bin/python

import sys
import re

f = open(sys.argv[1], 'rt')

for t in range(1, int(f.readline())+1):
	
	n, m = map(int, f.readline().split(' '))

	D = {}
	D_order = {}
	for i in range(n):
		word = f.readline().strip()
		D.setdefault(len(word), []).append(word)
		D_order[word] = i
		
	L = []
	for i in range(m):
		L.append(f.readline().strip())
		
	W0 = [(x, 0) for x in D.values()]
	
	S = []
	for l in L: # for every list
		W = W0
		b = 0
		bw = W[0][0][0]
		
		for c in l: # for every character c in the list
			W1 = []
			for w, s in W:	# for every group of words
				if len(w) == 1:	# too small!
					if s > b or (s == b and D_order[w[0]] < D_order[bw]):
						b = s
						bw = w[0]
					continue
										
				D = {}
				for word in w:
					sig = re.sub('[^%s]'%c, ' ', word)
					D.setdefault(sig, []).append(word)
				
				x = len(w[0])
				if len(D.keys()) > 1:
					w = [(D[k], s + (k == ' '*x)) for k in D.keys()]
				else:
					w = [(D[k], s) for k in D.keys()]
				
				W1.extend(w)
			
			W = W1
			#print W
			if not W:
				break
		
		S.append(bw)		
		
	print "Case #%d: %s" % (t, ' '.join(S))
