import sys

infile = sys.argv[1]
outfile = sys.argv[2]

inf = open(infile)
outf = open(outfile, 'w')

numTestCases = inf.readline()

def calculateTime(price, outputrate, remainder):
	array = []
	curoutput = 2.0
	nextoutput = 2.0+outputrate
	while ((remainder-price)/curoutput - remainder/nextoutput > 0):
		# print (remainder-price)/curoutput - remainder/nextoutput
		curoutput = 2+outputrate*(len(array))
		nextoutput = 2+outputrate*(len(array)+1)
		array += [price/curoutput]
		# print array[-1]#sum(array)
	# array = array[:-1]
	# array += [remainder/curoutput]
	return sum(array[:-1]+[remainder/curoutput])
def readTestCase(num):
	line = inf.readline().split()
	p = float(line[0])
	o = float(line[1])
	r = float(line[2])
	# print 'test case #' + num
	ans = calculateTime(p, o, r)
	outf.write('Case #' + num + ': %.7f \n' % ans)
for i in range(0, int(numTestCases)):
	readTestCase(str(i+1))