#!/usr/bin/python

f = open("input.txt")
items = int(f.readline())
counter = 0

def findHighOrderByte(num,maxVal=0x8000):
     if num & maxVal == maxVal:
          return maxVal
     return findHighOrderByte(num,maxVal >> 1)

while counter < items:
     counter+=1
     bagsize = int(f.readline())
     possibleToDo = 0
     candyList = []
     for x in f.readline().strip().split(" "):
          candyList.append(int(x))
          possibleToDo ^= int(x)
     candyList.sort()
     highOrderByte = findHighOrderByte(candyList[len(candyList)-1])
     if possibleToDo != 0:
          print "Case #"+str(counter)+": "+"NO"
          continue
     candyList.pop(0)
     for x in candyList:
          possibleToDo += x
     print "Case #"+str(counter)+": "+str(possibleToDo)

f.close()