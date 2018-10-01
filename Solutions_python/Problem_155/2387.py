from sys import *

def solve(inp1):
  shyMax = int(inp1[0])
  ShyPersons = inp1[1]
  PersonsRequiredTotal = 0
  PersonsRequiredCur = 0
  PersonsPresent = 0

  #print "shyMax: " + str(shyMax)
  for i in xrange(shyMax + 1):
    #print "A",i,PersonsPresent, ShyPersons[i]
    if i > PersonsPresent:
      PersonsRequiredCur = i - PersonsPresent
      PersonsRequiredTotal += PersonsRequiredCur
      PersonsPresent += PersonsRequiredCur
      #print PersonsRequiredCur, PersonsRequiredTotal, PersonsPresent
    PersonsPresent += int(ShyPersons[i])
    #print "P: " + str(PersonsPresent)

  return PersonsRequiredTotal


cases = int(raw_input())
for _ in xrange(cases):
  inp1 = map(str, stdin.readline().split())
  res = solve(inp1)

  print "Case #%d:" %(_+1), res
