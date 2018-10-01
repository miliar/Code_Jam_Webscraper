#!/usr/bim/env python

import sys

f = open(sys.argv[1])
g = open('output.txt','w')
n = int(f.readline().strip())

for i in xrange(n):
	line = [float(j) for j in f.readline().strip().split()]
	farm_cost = line[0]
	farm_rate = line[1]
	target = line[2]

	cps = 2.
	time = 0.

	while 1:
		#get to decision time point
		x = farm_cost / cps 
		time += x

		opt_1 = (target - farm_cost) / cps
		opt_2 = target / (cps + farm_rate)


		if opt_1 < opt_2:
			time += opt_1
			break
		else:
			cps += farm_rate

	output = "Case #"+str(i+1)+': '+ '%.7f' % time
	g.write(output+'\n')

f.close()
g.close()
