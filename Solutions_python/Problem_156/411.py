from math import ceil

def pancakes(d,p):
	pancakes = sorted(p)[::-1]
	a = pancakes[0]
	minutes = pancakes[0]
	for x in xrange(1,a+1):
		special = 0
		for y in pancakes:
			if y<=x:
				break
			special += ceil(float(y)/float(x))-1
		if special + x < minutes:
			minutes = special+x
	return int(minutes)

def read_and_write(readfrom,writein):
	inp = open(readfrom,'r')
	outp = open(writein, 'w')
	test = int(inp.readline().split(' ')[0])
	for i in xrange(test):
		a = map(int,inp.readline().split(' '))[0]
		b = map(int,inp.readline().split(' '))
		c = pancakes(a,b)
		outp.write("Case #%d: %d\n"%(i+1,c))
	inp.close()
	outp.close()

read = "B-large.in"
write = "B-large-output.txt"

read_and_write(read,write)