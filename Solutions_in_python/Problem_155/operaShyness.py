target = open('A-large.in', 'r')
testCases = target.readline()
caseList = []

for line in target:
	tempList = line.split(' ')
	shyArray = []
	maxShyness = tempList[0]

	for ch in tempList[1]:
		if ch.strip():
			shyArray.append(int(ch))
	caseList.append((maxShyness, shyArray))

target.close
requiredFriendArray = []

for case in caseList:
	i=0
	requiredFriend = 0
	maxShyness = int(case[0])
	shyArray = case[1]
	standingUp = 0

	for i in range(1, maxShyness+1):
		standingUp += shyArray[i-1]
		if standingUp < i and shyArray[i]>0:
			tempFriend = (i-standingUp)
			requiredFriend += tempFriend
			standingUp += tempFriend
	
	requiredFriendArray.append(requiredFriend)

target = open('shy.out', 'w')
n=0
for case in requiredFriendArray:
	target.write("Case #%i: %i\n" %(n+1, case))
	n += 1	
