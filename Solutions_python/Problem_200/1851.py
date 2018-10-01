numbersAmount = int(input())

for t in range(numbersAmount):
	currentNumber = list(input())
	for i in range(len(currentNumber)-1, 0, -1):
		if currentNumber[i-1] > currentNumber[i]:
			currentNumber[i-1] = str(int(currentNumber[i-1])-1)
			for j in range(i, len(currentNumber)):
				currentNumber[j] = "9"
	print("Case #{}: {}".format(t+1, int(''.join(currentNumber[0:len(currentNumber)]))))
