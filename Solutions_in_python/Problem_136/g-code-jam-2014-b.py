from sys import argv
from math import trunc


def floatList( L ):
	m = L.split(" ")
	for i in range(0,len(m)):
		m[i] = float(m[i])
	return m

def testCase(ln, args):
	#statements
	val = floatList(args)
	rate = 2.0
	time = 0.0
	c = val[0]
	f = val[1]
	x = val[2]	
	if x <= c:
		time = x/rate
	else:
		while True:
			if ( (x-c)/rate < x/(rate+f) ):
				time += x/rate
				break
			else:
				time += c/rate
				rate += f
	
	return "Case #%d: %.7f" % (ln,time)

script, fname = argv

fil = open(fname)
fol = open("g-code-jam-2014-b",'w')

N = int(fil.readline())

for i in range(0,N):
	fol.write( testCase( i+1, fil.readline() ) )
	if i < N-1:
		fol.write("\n")
