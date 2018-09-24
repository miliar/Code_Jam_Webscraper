#!/usr/bin/python
allData = [x.strip("\n") for x in open("A-small.in").readlines()]
i = 1; allCases = []

def makeDict(l):
 return dict(zip(l, [0 for x in l]))
def hasZero(l):
 return l.count(0)

while i < len(allData):
 thisCase = makeDict(allData[i + 1 : i + 1 + int(allData[i])])
 i += int(allData[i]) + 1
 thisCase = [thisCase, allData[i + 1 : i + 1 + int(allData[i])]]
 i += int(allData[i]) + 1
 allCases.append(thisCase)

for num in range(len(allCases)):
 i = 0
 case = allCases[num]
 for query in case[1]:
  case[0][query] += 1
  if not hasZero(case[0].values()):
   i += 1
   case[0] = makeDict(list(case[0]))
   case[0][query] += 1
 print "Case #%d:" % (num + 1), i
