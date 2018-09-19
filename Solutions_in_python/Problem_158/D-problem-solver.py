def omino(x,r,c):
	if r*c<x or r*c%x!=0 or ((r+c)/2.0<x-0.5):
		return "RICHARD"
	else:
		return "GABRIEL"

def read_and_write(readfrom,writein):
	inp = open(readfrom,'r')
	outp = open(writein, 'w')
	test = int(inp.readline().split(' ')[0])
	for i in xrange(test):
		a = map(int,inp.readline().split(' '))
		b = omino(a[0],a[1],a[2])
		outp.write("Case #%d: %s\n"%(i+1,b))
	inp.close()
	outp.close()

execute=raw_input("Test, small or large?: ")
read = "D-%s-attempt0.in"%(execute)
write = "D-%s-output.txt"%(execute)

read_and_write(read,write)