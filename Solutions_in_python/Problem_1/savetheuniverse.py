def main():
	infile = open("A-large.in","rU")
	outfile = open("outputalarge.txt","w")
	testcases = int(infile.readline())
#	print testcases
	for i in xrange(testcases):
		engines = {}
		switches = 0
		numengines = int(infile.readline())
		for j in xrange(numengines):
			inline = infile.readline()
			engines[inline] = 0
		numsearches = int(infile.readline())
		for k in xrange(numsearches):
			insearch = infile.readline()
			engines[insearch] = 1
			if checksum(engines) == numengines:
				switches += 1
				for key in engines:
					engines[key] = 0
				engines[insearch] = 1
		towrite = "Case #"+str(i+1)+": "+str(switches) + "\n"
		outfile.write(towrite)
	
def checksum(engines):
	sum = 0
	for key in engines:
		sum += engines[key]
	return sum

main()
