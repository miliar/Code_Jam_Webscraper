from Library import *
import math



def pairtime(less, more, goal, v):
	dless = goal - less[1]
	dmore = more[1] - goal
	dsum = dless + dmore
	rmore = (dless / dsum) * v
	rless = (dmore / dsum) * v
	t1 = (rless / less[0]) 
	t2 = (rmore / more[0])
	return max(t1, t2)

def fastestequal(equal):
	maxequal = 0
	for e in equal:
		maxequal += e[0]
	return maxequal

def solve(v, x, less, more, equal):
	if len(equal) == 0 and (len(more) == 0 or len(less) == 0):
		return False
	if (len(more) == 0 or len(less) == 0):
		return v / fastestequal(equal)
	minr = -1
	for l in less:
		for m in more:
			if minr == -1:
				minr = pairtime(l, m, x, v)
			else:
				minr = min(minr, pairtime(l, m, x, v))
	return minr

#
lines = getLines("b5.in")
out = []


# 1 line per case; 3 values per line
r = 0
for i in range(int(lines[0])):
	r += 1
	values = [float(l) for l in lines[r].split()]
	less = []
	more = []
	equal = []
	for j in range(int(values[0])):
		r += 1
		p = [float(l) for l in lines[r].split()]
		if p[1] > values[2]:
			more.append(p)
		elif p[1] < values[2]:
			less.append(p)
		else:
			equal.append(p)
	res = solve(values[1], values[2], less, more, equal)
	if res == False:
		out.append("Case #%d: IMPOSSIBLE"%(i + 1))
	else:
		out.append("Case #%d: %0.8f"%(i + 1, res))

#
writeOutLines("out.txt", out)