#! /usr/bin/env python


import datetime

def get_input(data):
	lines = data.split("\n")
	numCases = int(lines[0])
	taCount = 1
	caseCounter = 0
	inputCases = []
	while (caseCounter!=numCases):
		try:
				case = []
				case.append(lines[taCount])
				a, b = map(lambda x: int(x), lines[taCount+1].split())
				case.append(lines[taCount+2:taCount+2+a])
				case.append(lines[taCount+2+a:taCount+2+a+b])
				taCount += (2+a+b)
				inputCases.append(case)
				caseCounter += 1
		except:
			break
	return inputCases, numCases
		

def addTurnAroundTime(hhmm, t):
	hh,mm = hhmm.split(":")
	starttime = datetime.datetime(2008,07,17,int(hh), int(mm))
	interval = datetime.timedelta(minutes=int(t))
	endtime = starttime + interval 
	returnTimeStamp = "%02d" %(endtime.hour) + ":" + "%02d" %(endtime.minute)
	return returnTimeStamp


def checkAvailable(hhmm, available):
	try:
		if hhmm>=available[0]:
			return True
		else:
			return False
	except IndexError:
		return False


def addToAvailable(end, ta, available):
	newend = addTurnAroundTime(end, ta)
	available.append(newend)
	available.sort() # optimize this step
	return available
		
def getMaxTrains(ta, ttA, ttB):
	ttA.sort()
	ttB.sort()
	ta = int(ta)
	availableA = []
	availableB = []
	reqdA = 0
	reqdB = 0
	total = len(ttA) + len(ttB)
	while(total!=0):
		
		if len(ttB)==0 or (len(ttA)!=0 and ttA[0]<ttB[0]):
			start, end = ttA[0].split()
			status = checkAvailable(start, availableA)
			if status==False: 
				reqdA += 1
			else:
				availableA = availableA[1:]
			addToAvailable(end, ta, availableB)
			ttA = ttA[1:]
		elif len(ttB)!=0:
			start, end = ttB[0].split()
			status = checkAvailable(start, availableB)
			if status==False: 
				reqdB += 1
			else:
				availableB = availableB[1:]
			addToAvailable(end, ta, availableA)
			ttB = ttB[1:]

		total -= 1

	return str(reqdA), str(reqdB)

if __name__=="__main__":
	import sys

	try:
		#inputCases = [ ["2", ["09:00 09:01","12:00 12:02"], []]]
		inputCases, numCases = get_input(open(sys.argv[1]).read())
	except "M":
		print "Usage: ./MaxTrains.py <input-file-path>"
		sys.exit(0)


	for i in range(0,numCases):
		case = inputCases[i]
		maxTrains = getMaxTrains(case[0], case[1], case[2])
		print "Case #" + str(i+1) + ": " + maxTrains[0] + " " + maxTrains[1]
