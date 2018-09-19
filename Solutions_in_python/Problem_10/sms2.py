#! /usr/bin/python

inpfile = open('small.in','r')

inpCount = int (inpfile.readline())
ind = 0
case = 0

while ind < inpCount:
	line1 = inpfile.readline()
	(maxLetters,numKeys,numLetters) = line1.strip("\n").split(" ")
	maxLetters = int(maxLetters)
	numKeys = int(numKeys)
	numLetters = int(numLetters)
	freq1 = []
	freq = inpfile.readline().strip("\n").split(" ")
	for i in freq:
		freq1.append(int(i))
	#print freq1
	sortFreq = sorted(freq1)

	a = 1
	sum = 0
	count = 0

	if len(sortFreq) > numLetters or maxLetters * numKeys < numLetters:
		case = ind + 1
                print "Case #%d: Impossible" % (case)
                ind = ind + 1
	else:
		while a <= maxLetters:
			b = 1
			while b <= numKeys and count < numLetters:
				sum = sum + sortFreq[numLetters-count-1] * a
				#print sum
				#print sortFreq[numLetters-count-1]
				count = count + 1
				b = b+1
			a = a+1		
		#print sum

	        case = ind + 1
        	print "Case #%d: %d" % (case, sum)
	        ind = ind + 1

