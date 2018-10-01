#!/usr/bin/env python
def get_int_arr():
	return [int(x) for x in raw_input().split()]

def solve():
	line = raw_input().split()

	C = int(line.pop(0))
	combine = {}
	for i in range(C):
		v = line.pop(0)
		combine[v[0]+v[1]] = v[2]
		combine[v[1]+v[0]] = v[2]

	D = int(line.pop(0))
	oppose = {}
	for i in range(D):
		v = line.pop(0)
		oppose[v[0]] = v[1]
		oppose[v[1]] = v[0]
	
	N = int(line.pop(0))
	elist = []
	for elem in line.pop(0):
		elist.append(elem)
		# check for combination
		val = ''.join(elist[-2:])
		if val in combine:
			elist.pop()
			elist.pop()
			elist.append(combine[val])
		# check for oppose
		if elist[-1] in oppose:
			oppo = oppose[elist[-1]]
			if oppo in elist:
				elist = []
	return '['+', '.join(elist)+']'
				
t = get_int_arr()[0]
for x in range(t):
	print 'Case #%d: %s' % (x+1, solve())
