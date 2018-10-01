#!/usr/bin/env python

import copy

INPUT_FILE = 'A-large.in'

def process(case, engines, queries):
	switches = 0
	candidates = copy.copy(engines)

	while len(queries) > 0:
		if len(candidates) == 1:
			if candidates[0] == queries[0]:
				switches = switches + 1
				candidates = copy.copy(engines)
				continue
			else:
				queries.pop(0)
		else:
			if queries[0] in candidates:
				candidates.remove(queries[0])
			queries.pop(0)

	print 'Case #%d: %d' % (case, switches)

fp = open(INPUT_FILE, 'r')

n = int(fp.readline())

for case in range(1, n + 1):
	engines = []
	queries = []

	s = int(fp.readline())
	for j in range(s):
		engines.append(fp.readline().strip())
	
	q = int(fp.readline())
	for j in range(q):
		queries.append(fp.readline().strip())
	
	process(case, engines, queries)
