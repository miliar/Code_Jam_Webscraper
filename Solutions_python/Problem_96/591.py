import sys
from collections import defaultdict

t = input()

best, surp = defaultdict(set), defaultdict(set)

for i in range(11):
	best[i].add(3*i)
	if i >= 1:
		best[i].add(3*i - 1)
		best[i].add(3*i - 2)
	if i >= 2:
		surp[i].add(3*i - 3)
		surp[i].add(3*i - 4)

for i in range(10, -1, -1):
	best[i].update(best[i+1])
	surp[i].update(surp[i+1])

for i in xrange(t):
	line = sys.stdin.readline().split()
	n, s, p = map(int, line[:3])
	rest = map(int, line[3:])

	nsurp = 0
	nbest = 0

	for val in rest:
		if val in best[p]:
			nbest += 1
		elif val in surp[p]:
			nsurp += 1

	print "Case #{0}: {1}".format(i+1, nbest + min(s, nsurp))