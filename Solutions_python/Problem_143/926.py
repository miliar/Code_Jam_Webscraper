#!usr/bin/env python

from sys import argv

ansStr = "Case #%d: %d"
out = []
with open(argv[1]) as f_in:
	nCases = int(f_in.next())
	for case in xrange(nCases):
		a, b, k = map(int, f_in.next().split())
		winners = 0
		for i in xrange(a):
			for j in xrange(b):
				if i&j < k: winners += 1
						
		out.append(ansStr % (case+1, winners))
		# print '-' * 10

with open(__file__.replace('.py', '.out'), 'w') as f_out:
	for s in out:
		f_out.write(s + "\n")