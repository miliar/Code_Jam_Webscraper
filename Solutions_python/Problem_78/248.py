# Problem A
# Ameer Ayoub <ameer.ayoub@gmail.com>
from __future__ import division

def is_possible(n, d, g):
	for p in range(1,n+1):
		if p*(d/100) == int(p*(d/100)):
			if (g/100) == 1 and d != 100:
				return "Broken"
			elif (g/100) == 0 and d != 0:
				return "Broken"
			else:
				return "Possible"
	return "Broken"

f = open("A.in")
t = int(f.readline())
for i in range(t):
	case = map(int, f.readline().split())
	print "Case #{0}: {1}".format(i+1, is_possible(case[0], case[1], case[2]))
	