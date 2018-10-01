#!/usr/bin/python

import sys


def CalcRidesPerDay(numRides, capacity, numGroups, queue):

  #print "%d, %d, %d, %s" %(numRides, capacity, numGroups, str(queue))

  qPtr = 0
  totalRodeToday = 0
  totalThisRide = 0
  numGrpsThisRide = 0

  #some special cases for efficiency
  if numRides == 0 or capacity == 0 or numGroups == 0:
    return totalRodeToday

  if numGroups == 1 and queue[0] <= capacity:
    totalRodeToday = numRides * queue[0]
    return totalRodeToday

  # iterate while number of rides > 0
  while numRides:
    grpSize = queue[qPtr]

    # if group size is more than capacity, the queue will stop moving
    if grpSize > capacity:
      break

    #put the group in the roller coaster if size is less than capacity
    if (grpSize <= (capacity - totalThisRide)):
      #print "grpSize = %d" %grpSize
      
      totalThisRide += grpSize
      totalRodeToday += grpSize
      numGrpsThisRide += 1
      
      if totalThisRide == capacity or numGrpsThisRide == numGroups:
        totalThisRide = 0
        numGrpsThisRide = 0
        numRides -= 1

      qPtr += 1
      if (qPtr == numGroups):
        qPtr = 0

    else:
      #Next ride
      totalThisRide = 0
      numGrpsThisRide = 0
      numRides -= 1

  return totalRodeToday
    

#CalcRidesPerDay

def main():

  inputFile = open(sys.argv[1], 'r')

  count = 0
  case = 0
  lineCount = 0

  R = 0
  k = 0
  N = 0

  for line in inputFile:
    line = line.strip()

    if not count:
      count = int(line)
      case = 1
      lineCount = 1
      continue

    splitLine = line.split()
  
    queue = []
    if lineCount % 2:
      R = int(splitLine[0])
      k = int(splitLine[1])
      N = int(splitLine[2])

      if (N == 0):
        #print "totalRodeToday = %d" %0
        print "Case #%d: %d" %(case, 0)
        lineCount = lineCount + 1 
        case = case + 1
    else:
      for group in splitLine:
        queue.append(int(group))
      numRides = CalcRidesPerDay(R, k, N, queue)
      print "Case #%d: %d" %(case, numRides)
      case = case + 1

    lineCount = lineCount + 1
#main

if __name__ == "__main__":
  main()
