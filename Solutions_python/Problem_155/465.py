from sys import stdin

def proc(l):
	s = sum(l)
	r = reduce(lambda x,y:max(x,y[0])+y[1], enumerate(l), 0)
	return r-s

stdin.readline()
for id,line in enumerate(stdin,1):
	l = map(int, line.split()[1])
	print "Case #{}: {}".format(id, proc(l))
