#! /usr/bin/python
# ugh. so many stupid mistakes.

def solve():
	fp = open("input.txt", "r")
	numCases = int(fp.readline())
	for case in range(numCases):
		turnAroundTime = int(fp.readline())
		trips = fp.readline().strip("\n").split(" ")
		trips = map(int, trips)
		NA = range(trips[0])
		NB = range(trips[1])
		for trip in range(trips[0]):
			NA[trip] = fp.readline().strip("\n").split(" ") 
		for trip in range(trips[1]):
			NB[trip] = fp.readline().strip("\n").split(" ") 

		# sort by departure
		NA.sort(lambda x, y: cmp(x[0],y[0]))
		# sort by arrival
		NB.sort(lambda x, y: cmp(x[1],y[1]))
		# check how many A trains
		trainsA = countTrains(NA, NB, turnAroundTime)

		# sort by arrival
		NA.sort(lambda x, y: cmp(x[1],y[1]))
		# sort by departure
		NB.sort(lambda x, y: cmp(x[0],y[0]))
		trainsB = countTrains(NB, NA, turnAroundTime)
		print "Case #%d: %d %d" % (case+1, trainsA, trainsB)
	fp.close()
			
def countTrains(X, Y, turnAroundTime):
	"""Assumes that X is sorted by departure and Y is sorted by arrival."""
	trains = 0
	j = 0
	for i in range(len(X)):
		trains = trains + 1
		while j < len(Y):
			if(compareTime(Y[j][1], X[i][0], turnAroundTime)):
				trains = trains - 1
				j = j + 1
			break
	return trains

def compareTime(arival, departure, turnAroundTime):
	departure = map(int, departure.split(":"))
	arival = map(int, arival.split(":"))

	arival[1] = arival[1] + turnAroundTime
	if arival[1]>60:
		arival[0] = arival[0] + 1
		arival[1] = arival[1]%60

	if arival[0] > departure[0]:
		return 0
	elif arival[0] == departure[0] and arival[1]<=departure[1]:
		return 1
	elif arival[0] < departure[0]:
		return 1
	else:	
		return 0

if __name__ == "__main__":
	solve()
