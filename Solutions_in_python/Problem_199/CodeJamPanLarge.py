# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	numberArray = raw_input().split()	#limitNumber is highest number received
	pancakes = numberArray[0]
	pan = numberArray[1]
	#print(pancakes +" " + pan)
	numDigits = int(pan)
	index = 0
	panInBits = 0
	while index < numDigits:
		panInBits = (panInBits << 1) + 1
		index = index +1
	
	iter = 0
	index = 0
	numOfPancakes = len(pancakes)
	while index < (numOfPancakes - int(pan) +1):
		#print(str(index) + " "+ pancakes[index])
		if pancakes[index] == '-':
			index2 = 0
			iter = iter +1
			while index2 < int(pan):
				charToAdd = '-'
				if pancakes[index + index2] == '-':
					charToAdd = '+'
				pancakes = pancakes[:index + index2] + charToAdd + pancakes[index + index2 +1:]
				index2 = index2 +1
				#print(pancakes)
		index = index +1
	#print(pancakes)
	index = numOfPancakes - int(pan)
	while index < numOfPancakes:
		if pancakes[index] == '-':
			iter = -1
			break
		index = index +1
		
	if iter == -1:
		print("Case #" +str(i) +": IMPOSSIBLE")
	else:
		print("Case #" +str(i) +": " +str(iter))
	#print("Case #" +str(i) +": " + str(AfterDivide) +" "+ str(AfterDivide2))
  #print("Case #{}: {} {}".format(i, n + m, n * m))
  # check out .format's specification for more formatting options