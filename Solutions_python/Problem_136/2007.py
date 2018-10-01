formatString = "Case #{0}: {1:.7f}"

def main():
	with open("test.in") as f:
		content = f.readlines()

	testCasesCount = int(content[0])

	content = content[1:]

	for testCount in xrange(testCasesCount):
		line = [float(x) for x in content[testCount].strip().split(' ')]
		solve(testCount, line[0], line[1], line[2])

def farmCost(currentFarmCount, previousFarmCost, F):
	return previousFarmCost * (2.0 + F * max(0, currentFarmCount - 1)) / (2.0 + F * currentFarmCount)

def rate(currentFarmCount, F):
	return currentFarmCount * F + 2.0

def solve(testCount, C, F, X):
	if C < 0 or F < 0 or X < 0:
		print "", C, F, X
		raise "Constants must be non-negative"
	farmCount = 0
	currentTime = X / 1.0 / rate(farmCount, F)
	remainderTime = currentTime
	while True:
		timeToNextFarm = C / 1.0 / rate(farmCount, F)
		previousRemainderTime = remainderTime
		farmCount += 1
		remainderTime = X / 1.0 / rate(farmCount, F)
		nextTime = currentTime - previousRemainderTime + timeToNextFarm + remainderTime
		#print "cT,pRT,ttNF,rT", currentTime, previousRemainderTime, timeToNextFarm, remainderTime
		if nextTime > currentTime:
			printResult(testCount, currentTime)
			return
		else:
			currentTime = nextTime

def printResult(testCount, time):
	print str.format(formatString, testCount + 1, time)

if __name__ == "__main__":
	main()
