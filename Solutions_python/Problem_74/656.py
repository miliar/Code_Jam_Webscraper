import sys
filename = sys.argv[1]
file = open(filename, 'r')
cases = int(file.readline())
for n in range(1, cases+1):
	data = file.readline().strip('\n').split(' ')
	steps = int(data[0])
	pos = {'O':1, 'B':1}
	time = 0
	lastTime = 0
	lr = None
	#print 'Case #{}'.format(n)
	for st in range(1, steps*2, 2):
		robot = data[st]
		button = int(data[st+1])
		if lr == None:
			lr = robot
		#print 'Step: {} Robot: {} Position: {} Time: {} lastTime: {} lastRobot: {}'.format(st, robot, button,time, lastTime, lr)
		#print 'robot position'
		#print pos
		
		thisTime = abs(button - pos[robot])
		
		#print 'This Time: {}'.format(thisTime)
		if lr == robot:
			lastTime += thisTime+1
		else:
			thisTime -= lastTime
			if thisTime < 0:
				thisTime = 0
			lastTime = thisTime+1
		time += thisTime +1
		#print 'Total time: {}'.format(time)
		pos[robot] = button
		lr = robot
	print 'Case #{}: {}'.format(n, time)