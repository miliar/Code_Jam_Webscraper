f = open('B-large.in.txt', 'r')
numCases = int(f.readline())
x = 1
while x <= numCases:
	rate = 2.0
	info = f.readline()
	cost, increase, goal = info.split()
	cost, increase, goal = float(cost), float(increase), float(goal)
	finished = False
	totalTime = 0
	while not finished:
		currentRateTime = goal/rate
		nextRateTime = cost/rate + goal/(rate+increase)
		if currentRateTime <= nextRateTime:
			finished = True
			totalTime += currentRateTime
		else:
			totalTime += (cost/rate)
			rate += increase
	print 'Case #' + str(x) + ': ' + '{:1.7f}'.format(round(totalTime, 7))
	x += 1