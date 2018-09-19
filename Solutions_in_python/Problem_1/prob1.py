#!/usr/bin/python

import sys


# parsing

lines = [line.strip() for line in open(sys.argv[1]).readlines()]
consumed = 0

def consumeSome(num):
	consumedLines = lines[:num]
	lines[:] = lines[num:]
	return consumedLines

def consumeOneDigit():
	return int(consumeSome(1)[0])

def consumeClause():
	length = consumeOneDigit()
	return (length, consumeSome(length))


# main logic

numCases = consumeOneDigit()

for caseId in range(numCases):
	numEngines, engines = consumeClause()
	numQueries, queries = consumeClause()
	#print engines
	#print queries

	if numQueries==0:
		print 'Case #%i: 0' % (caseId+1)
	else:
		optimal = [0]*numEngines; optimal[engines.index(queries[0])] = None
		for queryId in range(1,numQueries):
			#print queryId, [x if x!=None else 9 for x in optimal]
			oldBlockerId = optimal.index(None)
			newBlockerId = engines.index(queries[queryId])
			if oldBlockerId!=newBlockerId:
				newOptimal = optimal
				newOptimal[oldBlockerId] = min(optimal[:oldBlockerId]+optimal[oldBlockerId+1:])+1
				newOptimal[newBlockerId] = None
	
		print 'Case #%i: %i' % (caseId+1, min([num for num in optimal if num!=None]))

	# case1: different engine
	# optimality: 

	# case2: same engine

#for start in range(4):
#	for end in range(4):
		




"""
class Case(object):
	

class SwitchMinimizer_DynamicProg

numCases = lines[]

for caseId in range()
# consume 

print ''
"""
