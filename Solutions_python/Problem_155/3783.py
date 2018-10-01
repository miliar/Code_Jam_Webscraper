import sys

numCases = sys.stdin.readline()

for case in xrange(int(numCases)):
	linesplit = sys.stdin.readline().split()
	total = 0
	index = 0
	while index <= int(linesplit[0]):
		num = int(linesplit[1][index])
		if num == 0 or num == '0':
			total += 1
			index += 1
		else:
			curindex = index
			numToLoop = int(linesplit[1][curindex])
			index += numToLoop
			i = 1
			while i <= numToLoop:
				if(curindex + i <= int(linesplit[0])):
					index += int(linesplit[1][curindex + i])
					numToLoop += int(linesplit[1][curindex + i])
				i += 1
	sys.stdout.write("Case #" + str(case+1) + ": " + str(total) + "\n")

