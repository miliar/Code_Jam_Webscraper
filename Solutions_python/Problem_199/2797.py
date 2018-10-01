def flipCakes(cakesList, start, flipper):
	happyFlip = "+"
	sadFlip = "-"
	end = start + flipper - 1
	while start <= end:
		if cakesList[start] == sadFlip:
			cakesList[start] = happyFlip
		else:
			cakesList[start] = sadFlip
		start += 1
	return cakesList

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(0, t):
	inputLine = input().split(" ")
	pancakes = inputLine[0]
	flipperSize = int(inputLine[1])
	happyFlip = "+"
	sadFlip = "-"

	pancakesList = list(pancakes)
	numPancakes = len(pancakesList) + 1
	flipCount = 0

	for cakeIndex in range(0, numPancakes - 1):
		cake = pancakesList[cakeIndex]
		if cake != happyFlip:
			# check if possible to flip
			if (cakeIndex + flipperSize) < numPancakes:
				pancakesList = flipCakes(pancakesList, cakeIndex, flipperSize)
				flipCount += 1
			else:
				flipCount = "IMPOSSIBLE"
				break;
	print("Case #{}: {}".format(i + 1, flipCount))
	# check out .format's specification for more formatting options