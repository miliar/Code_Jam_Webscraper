from __future__ import with_statement
#FILE = "b.input.small"
#FILE = "B-small-attempt0.in"
#FILE = "B-small-attempt1.in"
FILE = "B-large.in"

def parseTime(time):
	hours, minutes = map(int, time.split(":"))
	return hours * 60 + minutes

def sortMinimizeDepart(trip1, trip2):
	return trip1[1] - trip2[1]

def addTrain(station, time):
	global currentTrains
	currentTrains[station].append(time)

def getAvailableTrain(station, departTime):
	availableTrains = filter(lambda availTime: availTime <= departTime, currentTrains[station])
	if(len(availableTrains) == 0): return None
	return sorted(availableTrains)[0]

def otherStation(station):
	return {'A': 'B', 'B': 'A'}[station]

def moveTrain(station, depart, arrive):
	currentTrains[station].remove(depart)
	addTrain(otherStation(station), arrive + turnaroundTime)

with file(FILE, 'r') as f:
	numberOfCases = int(f.readline())
	testCase = 0

	for testCase in range(1, numberOfCases + 1):
		turnaroundTime = int(f.readline())
		numberAB,numberBA = map(int, f.readline().strip().split(' '))

		trips = [] #source, depart, arrive
		for _ in range(numberAB):
			depart, arrive = map(parseTime, f.readline().strip().split(' '))
			trips.append(('A', depart, arrive))
		for _ in range(numberBA):
			depart, arrive = map(parseTime, f.readline().strip().split(' '))
			trips.append(('B', depart, arrive))

		trips.sort(sortMinimizeDepart)

		startTrains = {'A': 0, 'B': 0}
		currentTrains = {'A': [], 'B': []}

		for trip in trips:
			station, depart, arrive = trip
			train = getAvailableTrain(station, depart)
			if train == None:
				addTrain(station, depart)
				startTrains[station] += 1
				train = depart
			moveTrain(station, train, arrive)

		print "Case #%d: %d %d" % (testCase, startTrains['A'], startTrains['B'])
