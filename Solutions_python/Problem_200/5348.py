#computer the exact arraay value ----------------
def compute(digits):
	# Cretae a max Count array
	maxCount = []
	curr = 0
	start = len(digits) - 1
	while start != -1:
		if curr == 0 :
			maxCount.append(digits[start])
		else:
			if digits[start] >= maxCount[curr-1] :
				maxCount.append(digits[start])
			else :
				maxCount.append(maxCount[curr-1])

		start -= 1
		curr += 1

	maxCount = list(reversed(maxCount))
	
	currentMax = 9
	# Now update the digit array
	for i in range(len(digits) - 1) :
		#print "digits array "  , digits
		#print "max count array ", maxCount	
		if digits[i] != maxCount[i] or maxCount[i] < digit[i+1] or digits[i+1] != maxCount[i+1]:
			
			digits[i] = max(digits[i+1], currentMax)
			maxCount[i] = digits[i]
			maxCount[i+1] -= 1
			digits[i+1] -= 1
			currentMax = digits[i]


	return digits

queries = int(input())
start = 1
while start <= queries :
	num = int(input())

	digit = []
	while (num >= 10) :
	    digit.append(num % 10)
	    num = num / 10
	if num < 10 :
		digit.append(num)

	if len(digit) == 1:
		print "Case #"+str(start)+str(":"), digit[0]
	else :
		ans = compute(digit)
		#remove leading zero's 
		values = []
		i = len(ans) - 1
		flag = True
		while i >= 0:
			if ans[i] == 0 and flag:
				pass
			else :
				flag = False
				values.append(ans[i])

			i -= 1
		ans = "".join([str(x) for x in values])
		print "Case #"+str(start)+str(":"), ans
	start += 1


