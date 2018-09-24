#!/usr/bin/python
import sys, psyco
psyco.full()

def crit(x,q,i):
	try:
		res = q.index(x,i)
	except ValueError:
		res = 10**7
	
	return res

def solve( case, s, q ):
	#print >> sys.stderr, s
	#print >> sys.stderr, q
	res = 0

	i = 0

	while i < len(q):
		choice = max(s,key=lambda x: crit(x,q,i))
		try:
			i = q.index(choice, i)
		except ValueError:
			break
		#print >> sys.stderr, i, choice
		res += 1

	print "Case #%d: %d" % (case, res)

first = True
N, S, Q = -1, -1, -1
state = ""
case = 1

searchengines = []
queries = []

for line in file( sys.argv[1] ):
	line = line[:-1]

	if first:
		N = int(line)
		state = "getS"
		first = False
		continue

	if state == "getS":
		S = int(line)
		state = "getNames"
		continue

	if state == "getNames":
		if len(searchengines) < S:
			searchengines.append( line )
		else:
			state = "getQueries"
			Q = int(line)
		continue

	if state == "getQueries":
		if len(queries) < Q:
			queries.append( line )
		else:
			S = int(line)

			solve( case, searchengines, queries )
			
			searchengines = []
			queries = []
			case += 1
			state = "getNames"
		continue

solve( case, searchengines, queries )
