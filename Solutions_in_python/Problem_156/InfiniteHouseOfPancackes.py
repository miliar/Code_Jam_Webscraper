import googleInput
import googleOutput

def calcSecsBruteForce(stacks):
	greatest = max(stacks)
	if greatest == 0:
		return 0
	least = greatest
	for i in range(2, (greatest / 2) + 1):
		temp = list(stacks)
		a = greatest - i
		b = i
		temp.remove(greatest)
		temp.append(a)
		temp.append(b)
		ans = calcSecsBruteForce(temp) + 1
		if ans < least:
			least = ans
	temp = list(stacks)
	for i in range(len(temp)):
		if temp[i] > 0:
			temp[i] -= 1
	ans = calcSecsBruteForce(temp) + 1
	if ans < least:
		least = ans
	return least

"""def calcSecs(stacks):
	special = 0
	while True:
		temp = list(stacks)
		greatest = max(stacks)
		greatestIndex = stacks.index(greatest)
		if len(stacks) > 1:
			temp.remove(greatest)
			secondGreatest = max(temp)
		else:
			secondGreatest = greatest
		found1 = False
		if stacks[greatestIndex] > 1:
			for i in range(2, stacks[greatestIndex]):
				if ((greatest / i) + (greatest % i)) + (i - 1) < secondGreatest + special:
					stacks[greatestIndex] = ((greatest / i) + (greatest % i))
					found1 = True
					special += (i - 1)
					break
		if not found1:
			return greatest + special"""

#print calcSecsBruteForce([])


inputClass = googleInput.ParseInput("pancackes.small.in.txt")
outputClass = googleOutput.OutputText("pancackes.small.out.txt")

parsed = inputClass.parseString(2, int)

for i in parsed:
	if type(i[1]) == int:
		outputClass.addToFile(calcSecsBruteForce([i[1]]), int)
	else:
		outputClass.addToFile(calcSecsBruteForce(i[1]), int)

inputClass.allDone()
outputClass.allDone()