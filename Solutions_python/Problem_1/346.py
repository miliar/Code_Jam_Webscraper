def lastleft (query, searchengines):
	last = 1
	for x in searchengines:
		if x[0] != query and x[1] == 0:
			last = 0
		if x[0] == query and x[1] != 0:
			last = 0
	return last
	
def mark (query, searchengines):
	for x in searchengines:
		if x[0] == query:
			x[1] = x[1] + 1
	return searchengines
			
def reset (searchengines):
	for x in searchengines:
		x[1] = 0
	return searchengines

import sys
f = open(sys.argv[1],'r')

N = int(f.readline())

for case in range(N):
	switches = 0
	S = int(f.readline())
	searchengines = []
	for x in range(S):
		searchengines = searchengines + [[(f.readline().strip()), 0]]
	Q = int(f.readline())
	for x in range(Q):
		query = (f.readline().strip())
		if lastleft (query, searchengines) == 1:
			switches = switches + 1
			searchengines = reset(searchengines)
			searchengines = mark(query, searchengines)
		else:
			searchengines = mark(query,searchengines)
	print "Case #%s: %s" %(case+1, switches)
		
	