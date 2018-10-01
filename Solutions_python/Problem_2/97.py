#!/usr/bin/python
import sys, psyco
from bisect import bisect
psyco.full()

def conv( times, T ):
	for i,v in enumerate(times):
		times[i] = [int(x) for x in v.replace(":"," ").split()]
		times[i] = ( times[i][0]*60 + times[i][1], \
					 times[i][2]*60 + times[i][3] + T )
		#if times[i][1] > 1440: del times[i]

def train( t1, t2 ):
	#print "trainCall!"
	p1, p2 = t1, t2
	j=0
	i = 0
	f="A"
	while 0<=j<len(p1):
		t = p1[j]
		del p1[j]
		j = bisect( p2, (t[1],0) )
		p1, p2 = p2, p1

		#debug
		if f == "A": 
			f="B"
		else: 
			f="A"
		#print f, j

		#i+=1
		#if i>20: 
			#print "overk1ll"
		#	break

def solve( case, T, timesAB, timesBA ):
	conv(timesAB, T)
	conv(timesBA, T)

	timesAB.sort()
	timesBA.sort()

	#print >> sys.stderr, T
	#print >> sys.stderr, timesAB
	#print >> sys.stderr, timesBA
	#print >> sys.stderr
	
	A,B = 0,0
	while len(timesAB) > 0 or len(timesBA) > 0:
		if len(timesAB) == 0:
			train( timesBA, timesAB )
			B+=1
		elif len(timesBA) == 0:
			train( timesAB, timesBA )
			A+=1
		else:
			if timesAB[0] <= timesBA[0]:
				train( timesAB, timesBA )
				A+=1
			else:
				train( timesBA, timesAB )
				B+=1
		
	
	print "Case #%d: %d %d" % (case, A, B)


first = True
state = ""
N, T, NA, NB = 0,0,0,0
timesAB = []
timesBA = []
case = 1

for line in file( sys.argv[1] ):
	line = line[:-1]

	if first:
		N = int(line)
		first = False
		state = "getT"
		continue

	if state == "getT":
		T = int(line)
		state = "getNA/NB"
		continue

	if state == "getNA/NB":
		cols = line.split()
		NA = int(cols[0])
		NB = int(cols[1])
		state = "getTimesNA"
		continue

	if state == "getTimesNA":
		if len(timesAB)<NA:
			timesAB.append(line)
		else:
			if NB > 0:
				timesBA.append(line)
				state = "getTimesNB"
			else:
				T = int(line)
				state = "getNA/NB"
				solve( case, T, timesAB, timesBA )
				case += 1
				timesAB = []
				timesBA = []
			continue

	if state == "getTimesNB":
		if len(timesBA)<NB:
			timesBA.append(line)
		else:
			state = "getNA/NB"

			solve( case, T, timesAB, timesBA )

			case += 1
			timesAB = []
			timesBA = []
			T = int(line)
			continue

solve( case, T, timesAB, timesBA )
