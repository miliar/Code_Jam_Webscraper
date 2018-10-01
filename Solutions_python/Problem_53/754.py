#!/usr/bin/python
import sys
import string


def findOnNumber(n):
  if n==1 :
    return 1
  else:
    return (2 * findOnNumber(n-1) + 1)

def findLightState(N, K):
  onK = findOnNumber(N)
  if (K + 1)%(onK + 1) == 0:
    return "ON"
  else: 
    return "OFF"

def main():
  in_fName= sys.argv[1]
  inputFile = open(sys.argv[1])
  caseCount = string.atoi(inputFile.readline())
  caseNum = 1

  for line in inputFile:
    cc = line.split()
    print ("Case #%s: " % caseNum) + findLightState(string.atoi(cc[0]),
        string.atoi(cc[1]))
    caseNum = caseNum + 1

main()
