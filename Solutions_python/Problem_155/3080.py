def standing_ovation_test(maxShyness, numberOfShyMembersPerShynessLevel):
  #print maxShyness, numberOfShyMembersPerShynessLevel
  #if maxShyness == 0: return 0
  numPeopleStanding = 0
  numPeopleNeeded = 0
  numPeople = len(numberOfShyMembersPerShynessLevel)
  numPeoplePerShynessLevel = {}
  #Convert list to dict

  for shynessLevel, numPeopleOnSameShynessLevel in enumerate(numberOfShyMembersPerShynessLevel):
    if int(shynessLevel) not in numPeoplePerShynessLevel.keys():
      numPeoplePerShynessLevel[int(shynessLevel)] = 0
    numPeoplePerShynessLevel[int(shynessLevel)] += int(numPeopleOnSameShynessLevel)
  #from pprint import pprint
  #pprint(numberOfShyMembersPerShynessLevel)
  #pprint(numPeoplePerShynessLevel)
  for shynessLevel in sorted(numPeoplePerShynessLevel.keys()):
    if shynessLevel == 0:
      numPeopleStanding += numPeoplePerShynessLevel[shynessLevel]
    elif shynessLevel <= numPeopleStanding:
      numPeopleStanding += numPeoplePerShynessLevel[shynessLevel]
    else:
      numPeopleNeeded += shynessLevel - numPeopleStanding
      numPeopleStanding += shynessLevel - numPeopleStanding + numPeoplePerShynessLevel[shynessLevel]
    #print "for shyness %d we have %d standing, %d needed"%(shynessLevel, numPeopleStanding, numPeopleNeeded)
  return numPeopleNeeded

def parse_input():
  num_test = int(raw_input().strip())
  testdb = {}
  for test_num in range(num_test):
    maxShyness, shynessMembersPerShynessLevel = raw_input().strip().split(" ")
    testdb[test_num] = (maxShyness, shynessMembersPerShynessLevel)

  for test_num in range(num_test):
    maxShyness, shynessMembersPerShynessLevel = testdb[test_num]
    print "Case #%d: %d"%(test_num+1,standing_ovation_test(maxShyness, shynessMembersPerShynessLevel))

if __name__ == "__main__":
  parse_input()
