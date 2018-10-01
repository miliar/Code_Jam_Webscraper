import sys
import math

def next_engine(engines, queries):
	winning_engine = ''
	winning_len = 1
	for engine in engines:
		this_len = 0
		for i in xrange(len(queries)):
			if queries[i] == engine:
				break
			this_len += 1
		if (this_len >= winning_len):
			winning_len = this_len
			winning_engine = engine
	return (winning_len, winning_engine)

def switchsearch(engines, queries):
	if len(queries) < 2:
		return '0'
	switches = 0
	i = 0
	prev_engine = ''
	while 1:
		run_len, engine = next_engine(engines, queries[i:])
		#print 'Engine: ' + engine
		i += run_len
		if len(queries) - 1 <= i:
			if engine != prev_engine and prev_engine != '' and run_len == 1:
				switches += 1
			break;
		switches += 1
		prev_engine = engine
	return str(switches)

n = int(raw_input('Test cases: '))
output = ''
for x in xrange(1, n+1):
	y = int(raw_input())
	engines = [ ]
	for yi in xrange(y):
		engines.append(raw_input())
	z = int(raw_input())
	queries = [ ]
	for zi in xrange(z):
		queries.append(raw_input())
	output += 'Case #' + str(x) + ': ' + switchsearch(engines, queries) + '\n'
print '\n' + output