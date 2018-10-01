from sys import argv
from itertools import repeat,izip,tee,chain


in_ = open(argv[1], 'r')
out = open(argv[2], 'w')

def grouppairs(iter):
	return izip(*[chain(iter)]*2)


def sizewise(iter, n):
	sum = 0
	groups = []

	for i,j in enumerate(iter):
		if sum+j <= n:
			sum += j
			groups.append(j)
		else:
			iter[:] = iter[i:] + groups
			break
#	print groups, iter
	return sum		


def sim(R,k,n,g):
	income = 0
#	print R, k, n, g
	for i in range(R):
		income += sizewise(g,k)
		#print g
		
	return income

lines = [a.rstrip() for a in in_]

runs = []
for i,j in grouppairs(lines[1:]):
	R, k, N = map(int, i.split(' '))
	g = map(int, j.split(' '))
	runs.append((R,k,N,g))

for i,run in enumerate(runs):
	R, k, N, g = run
	income = sim(R,k,N,g)

	out.write("Case #%d: %d\n" % (i+1, income))
	print "Case #%d: %d" % (i+1, income)

