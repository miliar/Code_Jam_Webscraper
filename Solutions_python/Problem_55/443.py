#!/usr/bin/python

rotate = lambda x: x[1:]+[x[0]]

filename = map(str.rstrip, open("C-small.in", 'r').readlines())
output = open("C-small.out", 'w')
t = int(filename[0])
counter = 1
for d in xrange(t):
	r, k, n = [int(x) for x in filename[counter].split(' ')]
	groups = [int(x) for x in filename[counter+1].split(' ')]
	euros = 0
	for y in xrange(r):
		tot = 0
		c = 0
		while tot<=k and c <= n:
			tot+=groups[0]
			groups = rotate(groups)
			c+=1
		euros+= tot-groups[-1]
		groups = [groups[-1]]+groups[:len(groups)-1]
	counter+=2
	case = "Case #" + str(d+1) + ":"
	print >>output, case, euros

