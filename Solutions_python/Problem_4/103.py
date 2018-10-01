f = open('A.large.in').read().split('\n')

line = 0
T = int(f[line])
line = line+1

case = 1

while line < len(f):
	n=int(f[line])
	line=line+1
	
	x = sorted([int(i) for i in f[line].split(' ')])
	y = sorted([int(i) for i in f[line+1].split(' ')])[::-1]
	line=line+2	
	
	s= sum([ x[i]*y[i] for i in range(n)])
	
	print "Case #%i: %i" % (case,s)
	case=case+1
	
