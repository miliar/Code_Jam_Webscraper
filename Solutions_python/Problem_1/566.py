#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It's not so organizated, but is not so bad
# to a brazilian programmer who are 17 years old

# without cache, deprecated
def _next_query_pos(engine, query_pos):
	"""Returns the position in queries[] where isn't possible
	do a search using engine starting at query_pos"""
	global engines
	global queries
	global queries_len
	
	ret = query_pos
	for query in queries[query_pos:]:
		#print ">",
		if engine == query:
			return ret
		ret = ret + 1
	return ret
	
# with cache
def next_query_pos(engine, query_pos):
	"""Returns the position in queries[] where isn't possible
	do a search using engine starting at query_pos"""
	global engines
	global queries
	global queries_len
	global cache
	
	# check in cache  first
	cache_entry = cache[engines.index(engine)]
	if (cache_entry != -1):
		return cache_entry
	
	ret = query_pos
	for query in queries[query_pos:]:
		#print ">",
		if engine == query:
			return ret
		else:
			# cache write
			if query in engines:
				index = engines.index(query)
				if (cache[index] == -1):
					cache[index] = ret
		ret += 1
	return ret
	
def deeper(query_pos):
	"""Returns switchs"""
	global engines
	global queries
	global queries_len
	global cache
	
	if queries_len == 0:
		return 0
	
	switchs = 0
	
	max = query_pos
	while True:
		# Init the cache
		cache = [-1] * len(engines)
		
		for engine in engines:
			i = next_query_pos(engine, query_pos)
			#print 'i: ', i
			if i > max:
				if i >= queries_len:
					#print 'max*: ', i
					return switchs
				max = i
				#print 'update_max: ', max
		#print 'switch'
		switchs += 1
		query_pos = max
	
def run_case():
	"""Read data and work on it, returns the number of switchs"""
	global engines
	global queries
	global queries_len
	
	S = int(raw_input())
	engines = []
	for x in range(S):
		engines.append(str(raw_input()))
	Q = int(raw_input())
	queries = []
	for x in range(Q):
		queries.append(str(raw_input()))

	# Data read, let's play with it
	#print engines, "\n", queries
	queries_len = Q
	return deeper(0)

# Program starts here
case_switchs = []

N = int(raw_input())

for x in range(N):
	case_switchs.append(run_case())

i = 1
for x in case_switchs:
	print "Case #%i: %i" % (i, x)
	i = i + 1
