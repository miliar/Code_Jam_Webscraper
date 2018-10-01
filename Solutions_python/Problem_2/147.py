#!/usr/bin/python
allData = [x.strip("\n") for x in open("B-small.in").readlines()]
i = 1; allCases = []

def formatTime(s):
 twoTimer = []
 for time in s.split():
  hm = [int(x) for x in time.split(":")]
  twoTimer.append(60 * hm[0] + hm[1])
 return twoTimer
def futureTimes(l, time):
 i = 0
 while l[i][0] < time:
  i += 1
 return i

while i < len(allData):
 thisCase = [int(allData[i])] #turnaround
 AB = allData[i + 1].split() #A to B, B to A
 i += 2
 thisCase.append(sorted([formatTime(x) for x in allData[i : i + int(AB[0])]]))
 i += int(AB[0])
 thisCase.append(sorted([formatTime(x) for x in allData[i : i + int(AB[1])]]))
 i += int(AB[1])
 allCases.append(thisCase)

for num in range(len(allCases)):
 numTrains = [0, 0]
 case = allCases[num]
 while case[1] and case[2]:
  if case[1][0][0] < case[2][0][0]: currentTrain = [0, case[1].pop(0)[1]]
  else: currentTrain = [1, case[2].pop(0)[1]]
  numTrains[currentTrain[0]] += 1
  while 1:
   nextStop = case[1 + (not currentTrain[0])]
   #print currentTrain, nextStop
   try:
    currentTrain = [1 - currentTrain[0], nextStop.pop(futureTimes(nextStop, currentTrain[1] + case[0]))[1]]
   except: break

 numTrains[0] += len(case[1])
 numTrains[1] += len(case[2])
 print "Case #%d:" % (num + 1), numTrains[0], numTrains[1]
