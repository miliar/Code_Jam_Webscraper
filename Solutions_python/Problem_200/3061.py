def deleteLeadingZeroes(leadingZeroNumber):
	lzLoopLength = len(leadingZeroNumber)
	for i in xrange(0, lzLoopLength):
		if leadingZeroNumber[i] != "0":
			return leadingZeroNumber[i:]

def constructNumber(unsortedNumber, n):
	return unsortedNumber[:n] + str(int(unsortedNumber[n]) - 1) + ("9" * (len(unsortedNumber) - n - 1))

def sort(number):
	if(len(number) == 1):
		return number
	i = 0
	loopLength = len(number) - 1
	while i < loopLength:
		if number[i] <= number[i+1]:
			i += 1
		else:
			number = constructNumber(number, i)
			i = 0
	if number[0] == "0":
		return deleteLeadingZeroes(number)
	else:
		return number

t = int(raw_input())
for i in xrange(1, t + 1):
	n = [s for s in raw_input().split(" ")]
	#print sort(n[0])
	print "Case #{}: {}".format(i, sort(n[0]))