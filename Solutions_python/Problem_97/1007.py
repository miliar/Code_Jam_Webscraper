from collections import deque
from copy import copy

def solve_one(line):
	"""terrible"""
	sa, sb = line.split(" ")
	da, db = deque(sa), deque(sb)
	a, b = int(sa), int(sb)
	rot = range(len(sa)-1)
	found = 0
	for n in xrange(a, b): # n < m so n < b
		dn = deque(str(n))
		dm = copy(dn)
		found_here = set()
		for _ in rot:
			dm.rotate()
			if dn < dm <= db:
				found_here.add(tuple(dm))
		found += len(found_here)
	return found

def solve(inp):
	output = []
	for line, i in zip(inp.split("\n")[1:], range(1, 1000)):
		output.append("Case #%d: %s" % (i, solve_one(line)),)
	result = "\n".join(output)
	open("C.out", "w").write(result)
	return result
