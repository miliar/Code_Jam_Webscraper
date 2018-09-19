#!/usr/bin/python

# Daniel Bungert <danielbungert@gmail.com>

import sys

cases = int(sys.stdin.readline())

for case in range(1, cases + 1):
	full = 0

	num_engines = int(sys.stdin.readline())
	engines = {}
	for i in range(num_engines):
		engine = sys.stdin.readline().strip().lower()
		engines[engine] = 1 << i
		full |= engines[engine]

	queries = []
	num_queries = int(sys.stdin.readline())
	for i in range(num_queries):
		query = sys.stdin.readline().strip().lower()
		queries.append(query)

	bm = 0
	switches = 0
	for query in queries:
		bm |= engines[query]
		if bm == full:
			switches += 1
			bm = engines[query]

	ans = switches

	print 'Case #%d: %d' % (case, ans)
