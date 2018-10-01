#!/usr/bin/python3

import sys

def parse(filename):
  f = open(filename)
  numTestCases = int(f.readline())
  numtestmax = numTestCases + 1
  while numTestCases:
    print ("Case #" + str(numtestmax - numTestCases) + ": ", end='')
    user1 = int(f.readline())
    rows1 = []
    rows2 = []
#read first input
    for i in range(1,5):
      if i == user1:
        rows1 = f.readline().strip().split(" ")
      else:
        f.readline()
#read second input
    user2 = int(f.readline())
    for i in range(1,5):
      if i == user2:
        rows2 = f.readline().strip().split(" ")
      else:
        f.readline()
#perform the check
    numPossibilities = 0
    value = 0
    while rows1:
      testVal1 = rows1.pop()
      for testVal2 in rows2:
        if testVal1 == testVal2:
          numPossibilities += 1
          value = testVal2
    if numPossibilities == 0:
      print ("Volunteer cheated!")
    elif numPossibilities == 1:
      print (value)
    else:
      print ("Bad magician!")

#dec numTestCases
    numTestCases -= 1


def main():
  parse(sys.argv[1])


main()
