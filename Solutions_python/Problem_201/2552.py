def findMin(LsRs):

	chosen = 0

	if len(LsRs) == 1:
		minIndex = min(LsRs)
		minTuple = LsRs[minIndex]
		chosen = minTuple[0]
	else:
		minIndex = min(LsRs)
		minTuple = LsRs[minIndex]
		for key in sorted(LsRs):
			currentIndex = key
			currentTuple = LsRs[currentIndex]
			if min(currentTuple) > min(minTuple):
				minIndex = currentIndex
				minTuple = currentTuple
			elif min(currentTuple) == min(minTuple):
				if max(currentTuple) > max(minTuple):
					minIndex = currentIndex
					minTuple = currentTuple
				elif max(currentTuple) == max(minTuple):
					if currentIndex < minIndex:
						minIndex = currentIndex
						minTuple = currentTuple

		chosen = minIndex

	return chosen, minTuple

def updateStalls(stalls, chosen):

	newStalls = list()
	updated = []

	for stall in stalls:
		if chosen not in stall:
			newStalls.append(stall)
		else:
			if len(stall) > 1:
				index = stall.index(chosen)
				temp0 = stall[0:index]
				temp1 = stall[index+1:]
				if temp0:
					newStalls.append(temp0)
					updated.append(len(newStalls) - 1)
				if temp1:
					newStalls.append(temp1)
					updated.append(len(newStalls) - 1)

	return newStalls, updated

def generateLsRs(stalls, index):

	Ls = 0
	Rs = 0

	for i in range(index - 1, -1, -1):
		if stalls[i] is True:
			break
		Ls += 1

	for i in range(index + 1, len(stalls), 1):
		if stalls[i] is True:
			break
		Rs += 1

	return Ls, Rs

def process(n, k):

	stalls = [False] * (n + 2)
	stalls[0] = True
	stalls[-1] = True

	y = 0
	z = 0

	#
	ListOfLists = [[i for i in range(1, n + 1, 1)]]
	helpfulDict = dict()
	for List in ListOfLists:
		for i in range(0, len(List), 1):
			helpfulDict[List[i]] = [i, len(List) - i - 1]

	#
	chosen, minTuple = findMin(helpfulDict)
	ListOfLists, updated = updateStalls(ListOfLists, chosen)
	helpfulDict.pop(chosen, None)
	if updated:
		for update in updated:
			for i in range(0, len(ListOfLists[update]), 1):
				helpfulDict[ListOfLists[update][i]] = [i, len(ListOfLists[update]) - i - 1]

	for j in range(1, k, 1):
		chosen, minTuple = findMin(helpfulDict)
		ListOfLists, updated = updateStalls(ListOfLists, chosen)
		helpfulDict.pop(chosen, None)
		if updated:
			for update in updated:
				for i in range(0, len(ListOfLists[update]), 1):
					helpfulDict[ListOfLists[update][i]] = [i, len(ListOfLists[update]) - i - 1]

	y = max(minTuple)
	z = min(minTuple)

	'''
	LsRs = dict()
	for i in range(1, n + 1, 1):
		LsRs[i] = [i-1, n-i]

	for i in range(0, k, 1):

		print(LsRs)

		chosen, minTuple = findMin(LsRs)

		dL, dR = LsRs[chosen]
		print(chosen, dL, dR)

		for j in range(1, chosen, 1):
			if j in LsRs:
				LsRs[j][1] -= dR

		for j in range(chosen + 1, n + 1, 1):
			if j in LsRs:
				LsRs[j][0] -= dR

		print(LsRs)

		y, z = LsRs.pop(chosen, None)

		print(LsRs)
		print(chosen, y, z)
		print("")

	#for i in range(0, chosen, 1):
	#	LsRs[i][1][1] -= chosen

	#print(LsRs)

	for i in range(0, k, 1):

		LsRs = list()

		for i in range(1, len(stalls) - 1, 1):
			if stalls[i] is False:
				LsRs.append((i, generateLsRs(stalls, i)))

		y, z, chosen = findMin(LsRs)
		stalls[chosen] = True

	'''

	return y, z

def main():

	if True:
		t = int(input())
		for i in range(1, t + 1):
		  n, k = input().split(" ")
		  y, z = process(int(n), int(k))
		  print("Case #" + str(i) + ":", y, z)
	else:
		n, k = "5 2".split(" ")
		y, z = process(int(n), int(k))
		print(y, z)

if __name__ == "__main__":
	main()