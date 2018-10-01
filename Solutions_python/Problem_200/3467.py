# split the number up into single ints

# iterate over list from right to left

# if a number is greater than the number that preceded it,
# decrement the number by 1

# set the predecessor and all previous values equal to 9

import sys
import fileinput

numTestCases = None
testCase = 0

for line in fileinput.input():
  if fileinput.isfirstline():
    numTestCases = int(line.rstrip())
    continue
  testCase += 1
  test = line.rstrip()

  numArray = [int(x) for x in list(test)]

  stopInd = len(numArray)

  prevNum = numArray[-1]
  #iterate in reverse order
  for index in reversed(range(len(numArray) - 1)):
    if numArray[index] > prevNum:
      numArray[index] = numArray[index] - 1
      for indexPrime in range(index+1, stopInd):
        numArray[indexPrime] = 9
      stopInd = index+1
    prevNum = numArray[index]
  print "Case #"+str(testCase)+": "+str(int(''.join([str(x) for x in numArray])))



