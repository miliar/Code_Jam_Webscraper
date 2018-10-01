from itertools import *		
from math import *	

HD = 720

inf = open("b.in", 'r')
outf = open("b.out", 'w')

t = int(inf.readline())

for tc in xrange(0, t):
	ac, aj = map(int, inf.readline().split())
	c =[]
	d = []
	j = []
	k = []
	for i in xrange(0, ac):
		tmp = 	map(int, inf.readline().split())
		c.append(tmp[0])
		d.append(tmp[1])
	for i in xrange(0, aj):
		tmp = 	map(int, inf.readline().split())
		j.append(tmp[0])
		k.append(tmp[1])
	c.sort()
	d.sort()
	j.sort()
	k.sort()
	print zip(c, d)
	print zip(j, k)
	
	res = 2
	if (aj == 0):
		if (ac < 2) or (d[1] - c[0] <= HD):
			pass
		else:
			if (c[1] - d[0] < HD):
				res = 4
				
	elif (ac == 0):
		if (aj < 2) or (k[1] - j[0] <= HD):
			pass
		else:
			if (j[1] - k[0] < HD):
				res = 4
	
	outf.write("Case #" + str(tc + 1) + ": ")	
	outf.write( str(res) + "\n")	
	
	
		
	
	
	
	
