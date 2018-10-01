import math


def solve(c, f, x):
# c = cost of farm
# f = extra cookies per second
# x = cookies needed
	cookiesPerSec = 2
	time = 0
	reachedX = False

	while not reachedX:
		timeToX = x / cookiesPerSec
		timeToXwithFarm = c / cookiesPerSec + x / (cookiesPerSec + f)
		if (timeToXwithFarm < timeToX):
			time += c / cookiesPerSec
			cookiesPerSec += f
		else:
			time += x / cookiesPerSec
			reachedX = True
	return time


name = "B-large"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split(" ")
	c = line[0]
	f = line[1]
	x = line[2]

	fout.write("Case #" + str(i + 1) + ": " + str(solve(float(c), float(f), float(x))) + "\n")
	#print "Case #" + str(i + 1) + ": " + str(solve(float(c), float(f), float(x))) + "\n"

fi.close()
fout.close()