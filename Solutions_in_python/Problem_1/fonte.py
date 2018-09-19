#!/usr/bin/env python

n = input()
for i in range(1, n+1):
	num_engines = input()
	
	engines = set()
	for j in range(num_engines):
		engines.add(raw_input())
		
	num_queries = input()
	
	queries = []
	for j in range(num_queries):
		query = raw_input()
		queries.insert(0, query)
		
	print "Case #%d:" % (i),
	
	conj_temp = set()
	cont = 0
	
	while queries != []:
		while engines != conj_temp:
			if queries == []:
				break
			query = queries.pop()
			conj_temp.add(query)
		if engines != conj_temp:
			break
		cont += 1
		conj_temp = set()
		conj_temp.add(query)
		
	print cont
