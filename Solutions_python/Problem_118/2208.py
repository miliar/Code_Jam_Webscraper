import math
inFileName = "in.txt"
outFileName = "out.txt"

def isPalindrome(num):
	return str(num) == str(num)[::-1]

def countNums(low, high):
	count = 0
	for num in range(low, high+1):
		if isPalindrome(num) and math.sqrt(num).is_integer() and isPalindrome(int(math.sqrt(num))):
			count += 1
	return count

f = open(inFileName, 'r')
numCases = f.readline().rstrip()
cases = []

for line in f:
	a, b = line.rstrip().split()
	cases.append([int(a), int(b)])

f.close()

f = open(outFileName, 'w')

caseNum = 1

for case in cases:
	f.write("Case #" + str(caseNum) + ": " + str(countNums(case[0], case[1])) + "\n")
	caseNum += 1