import math


def solve(maxShy, shy):

	numP = 0
	shy = list(shy)
	shy = map(int, shy)
	for i in range(0, maxShy):
		if sum(shy[0:i+1]) < (i + 1):
			numP += 1
			shy[i] += 1
	return str(numP)


name = "A-large"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split(" ")
	#line = map(int, line)

	fout.write("Case #" + str(i + 1) + ": " + solve(int(line[0]), line[1]) + "\n")
	print "Case #" + str(i + 1) + ": " + solve(int(line[0]), line[1])

fi.close()
fout.close()