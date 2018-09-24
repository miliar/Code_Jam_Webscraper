#!/usr/bin/env python

#sys.argv[1]: in file name
#sys.argv[2]: out file name

import sys, os, math, urllib

def solve_problem(search_engs, queries):
	
	switches = 0
	
	"""first, we need to construct a list for each engine that 
	shows to which queries that engine is valid"""
	
	engs_lists = []
	for engine in search_engs:
		engs_lists.append([])
	
	for query in queries:
		for engine in search_engs:
			eng_idx = search_engs.index(engine)

			if engine==query:
				engs_lists[eng_idx].append(0)
			else:
				engs_lists[eng_idx].append(1)
	

	#print engs_lists
	
	"""We need now to switch between engines such that we always select 
	the engine that spans the largest number of queries starting from 
	the current query"""
	
	
	first_time = True

	#index if engine can handle query, -1 otherwise, 
	#len=number of engines
	engs_status = []
	prev_engs_status = []
	engs_span = []
	

	for i in range( len(search_engs) ):
		engs_span.append(0)	

	prev_query_idx = 0

	for curr_query_idx in range( len(queries) ):
		for eng_list in engs_lists:	
			eng_idx = engs_lists.index(eng_list)
			
			if engs_span[eng_idx] <> curr_query_idx:
				engs_span[eng_idx] = eng_list[curr_query_idx]
			else:
				if eng_list[curr_query_idx] <> 0:
					engs_span[eng_idx] += eng_list[curr_query_idx]
				else:
					engs_span[eng_idx] = eng_list[curr_query_idx]
					
	

		if (curr_query_idx+1) not in engs_span:
			switches += 1
			
			for i in range( len(engs_span) ):
				if engs_span[i]==1:
					engs_span[i] = curr_query_idx + 1
				else:
					engs_span[i] = 0
		print engs_span			
				
	return switches	

def main():

	if len(sys.argv) <> 3:
		print 'usage: %s [in file] [out file]' %sys.argv[0]
		return


	fi = open( sys.argv[1], 'r')
	fo = open( sys.argv[2], 'w')
	

	no_cases = int( fi.readline() )
	
	for i in range(no_cases):
		search_engs = []
		queries = []

		no_search_engs = int( fi.readline() )
		for j in range(no_search_engs):
			search_engs.append( fi.readline() )

		no_queries = int( fi.readline() )
		for j in range(no_queries):
			queries.append( fi.readline() )

		
		no_switches = solve_problem(search_engs, queries)
		fo.write('Case #%d: %d\n' %(i+1, no_switches) )
		print '\n\n'
	
	fi.close()
	fo.close()


if __name__ == '__main__':
        main()


