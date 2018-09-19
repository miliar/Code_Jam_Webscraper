import math

filename="input"

f=open(filename,"r")
cases = int(f.readline())
x=0

while x < cases:
	x+=1
	sz=(f.readline()).split()
	N=int(sz[0])
	K=int(sz[1])
	status = "OFF"

	if ((K + 1) % math.pow(2,N)) == 0: status = "ON"
	print "Case #%d: %s" % (x, status)

