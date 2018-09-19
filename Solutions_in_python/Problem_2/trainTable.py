#!/usr/bin/python


def getMinutes(time):
	(hour, minute) = time.split(':')
	hour = int(hour.strip())
	minute = int(minute.strip())
	
	return hour * 60 + minute
	

def normalize5(s):
	temp = s
	for i in range(5-len(s)):
		temp = '$' + temp
		
	return temp

def getTimeTable(table,station):
	timeTable = {}
	
	trash = 0
	for el in table:
		trash = trash + 1
		(dep,arr) = el.split()
		dep = getMinutes(dep.strip())
		arr = getMinutes(arr.strip())
		
		index = normalize5(str(dep))+station
		if timeTable.has_key(index):
			timeTable[index+'x'+str(trash)] = arr
		else:
			timeTable[index] = arr
		
	return timeTable

def getTrain(trainList, station, depTime):
	keyList = trainList.keys()
	
	index = -1
	
	for key in trainList.keys():
		(st, arrTime) = trainList[key]
		if st == station and arrTime <= depTime:
			index = key
			break
	
	return index



def processTimeTables(timeTableA, timeTableB, turnAround):
	noTrainsA = 0
	noTrainsB = 0
	
	trainList = {}
	
	completeDepList = list()
	completeDepList.extend(timeTableA.keys())
	completeDepList.extend(timeTableB.keys())
	completeDepList.sort()
	i = 0
	#print timeTableA
	#print timeTableB
	#print completeDepList
	
	for dep in completeDepList:
		i = i + 1
		
		if timeTableA.has_key(dep):
			dTime = dep.split('x')
			dTime = dTime[0].strip('A')
			dTime = dTime.lstrip('$')
			dTime = int(dTime)
			#print dTime
			index = getTrain(trainList, 'A', dTime)
			if index == -1:
				trainList['A'+str(dep)+'x'+str(i)] = ('B', timeTableA[dep]+turnAround)
				noTrainsA = noTrainsA + 1
			else:
				trainList[index] = ('B', timeTableA[dep]+turnAround)
				
		if timeTableB.has_key(dep):
			dTime = dep.split('x')
			dTime = dTime[0].strip('B')
			dTime = dTime.lstrip('$')
			dTime = int(dTime)
		
			#print dTime
			index = getTrain(trainList, 'B', dTime)
			if index == -1:
				trainList['B'+str(dep)+'x'+str(i)] = ('A', timeTableB[dep]+turnAround)
				noTrainsB = noTrainsB + 1
			else:
				trainList[index] = ('A', timeTableB[dep]+turnAround)
	
	#print trainList
	
	return (noTrainsA, noTrainsB)

f = open('B-large.in', 'r')
noCases = f.readline()
noCases = int(noCases)

for i in range(noCases):
	turnAround = f.readline()
	turnAround = int(turnAround.strip())
	na = f.readline()
	na = na.strip()
	(na,nb) = na.split()
	na = int(na.strip())
	nb = int(nb.strip())
	tableA = list()
	tableB = list()
	for j in range(na):
		tableA.append(f.readline())
	for j in range(nb):
		tableB.append(f.readline())
	timeTableA = getTimeTable(tableA, 'A')
	timeTableB = getTimeTable(tableB, 'B')
	
	(noTrainsA, noTrainsB) = processTimeTables(timeTableA, timeTableB, turnAround)
	
	print 'Case #' + str(i+1) + ': ' + str(noTrainsA) + ' ' + str(noTrainsB)

f.close()