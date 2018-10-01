f = open('A-large.in', 'r')
fOut = open('A-large.out', 'w')
t = int(f.readline())
for i in xrange(1, t+1):
	data = f.readline().split()
	data[0] = int(data[0])
	numClapping = 0
	numInserts = 0
	for j in xrange(data[0] + 1):
		if (numClapping < j):
			numInserts += j - numClapping
			numClapping = j
		numClapping += int(data[1][j])
	fOut.write("Case #" + str(i) + ": " + str(numInserts) + "\n")
f.close()
fOut.close()


