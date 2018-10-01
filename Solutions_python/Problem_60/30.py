#!python
import copy
from collections import deque
from optparse import OptionParser
usage = "usage: %prog input"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()
if not args:
	parser.error("input omitted")
f = open(args[0])
T = int(f.readline())

for i in range(1,T+1):
	N,K,B,T = ( int(x) for x in f.readline().split() )
	# finish at time T
	# N chickens
	# B is location of barn
	# need K chickens home
	Xes = [ int(x) for x in f.readline().split() ]	# increasing
	Ves = [ int(x) for x in f.readline().split() ]
	#print N,K,B,T
	potential_ends = [ X + T*V for (X,V) in zip(Xes,Ves) ]
	potential_home = [ x>=B for x in potential_ends]
	#print Xes
	#print Ves
	#print potential_ends
	#print potential_home
	
	nec = []
	for j in range(N):
		if potential_home[j]:
			x = 0
			for what in potential_home[j+1:]:
				 if not what:
					x += 1
			nec.append(x)
	#print nec
	if sum(potential_home)<K:
		answer = "IMPOSSIBLE"
	else:
		home = 0
		#nec2 = sorted(nec)
		nec2 = nec[:]
		#print nec2
		swaps = 0
		while home < K:
			swaps += nec2.pop()
			home += 1
			
		answer = swaps
	print "Case #%d: %s" % (i,answer)
	#print
	pass