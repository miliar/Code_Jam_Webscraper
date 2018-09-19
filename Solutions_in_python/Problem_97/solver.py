import sys

def test(aSet, limit):
	a = set()
	size = len(aSet)
	for i in range(size-1):
		pre = aSet[len(aSet)-(i+1):]
		post = aSet[:len(aSet)-(i+1)]
		val = int(pre+post)
		if val <= limit and int(pre[0]) > 0 and pre+post != aSet and int(aSet) < val:
			a.add(val)
			
	return len(a)




def tester(lowerNumber, upperNumber):
	lowLimit = int(lowerNumber)
	upLimit = int(upperNumber)
	counter = 0
	if len(upperNumber) < 2:
		return 0
	else:
		while(lowLimit < upLimit):
			counter = counter + test(str(lowLimit), upLimit)
			lowLimit = lowLimit+1
	return counter



input_file = open(sys.argv[1], "r")
output_file = open(sys.argv[2], "w")

cases = int(input_file.next())

for i in range(cases):
	limits = map(lambda x: x.strip(),input_file.next().split(" "))
	result = tester(limits[0], limits[1])
	output_file.write("Case #{0}: {1}\n".format(i+1, result))

input_file.close()
output_file.close()