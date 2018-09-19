import math
f = open('D-small-attempt1.in', 'r')
o = open('1.out', 'w')

T = int(f.readline().strip())


for t in xrange(T):
	p = map(int, f.readline().strip().split(' '))
	x = p[0]
	r = p[1]
	c = p[2]
	p1="RICHARD"	
	p2="GABRIEL"
	area = r * c
	winner = p2
	if 	(area%x != 0) or (x>area) or (x>r and x>c) or (x/2.0>r) or (x/2.0>c) or (x>6) or(x==4 and (r==2 or c==2)):
		winner = p1
	out = "Case #" + str(t+1) + ": " + winner + "\n"
	o.write(out)
	print out	 