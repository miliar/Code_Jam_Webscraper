
"""

Basic idea:
	Brute force it, but make it a little faster by phrasing it as an XOR question
	Basically, we start with the pancake string and try XORing it by binary strings
		where the string has a 1 in the places where a pancake is flipped.
	Our goal is to get to the string with all ones.

"""

numInputs = int(input())

for case in range(1, numInputs + 1):
	S, K = input().split(" ") # taken from the quickstart guide
	K = int(K)
	numPancakes = len(S)
	pancakesDec = 0 # convert the (binary-ish) pancake row into a decimal number
	for digit in S[::-1]:
		pancakesDec *= 2
		if digit == "+":
			pancakesDec += 1
	goal = (2**numPancakes) - 1 # all ones in the binary representation
	if goal == pancakesDec:
		print("Case #" + str(case) + ": 0") # pancakes already all good, so no flips needed
		continue # move on to the next input
	prevFlip = (2**K) - 1 # binary representation corresponds to flipping the K rightmost pancakes
	potentialFlips = {prevFlip}
	while prevFlip < 2**(numPancakes - 1):
		potentialFlips.add(2 * prevFlip) # multiplying by 2 shifts the bits one to the left
		prevFlip *= 2
	previouslyFound = {pancakesDec}
	lastLevel = {pancakesDec}
	currLevel = 1
	success = False
	while len(lastLevel) > 0:
		nextLevel = set()
		for arrangement in lastLevel:
			for flip in potentialFlips:
				newArrangement = arrangement ^ flip
				if newArrangement == goal:
					print("Case #" + str(case) + ": " + str(currLevel)) # reached our goal state, so we're done
					success = True
					break # no need to do any further calculations for this input
				if newArrangement not in previouslyFound:
					previouslyFound.add(newArrangement)
					nextLevel.add(newArrangement)
				# if we have previously found this arrangement, ignore it
			if success:
				break
		if success:
			break
		lastLevel = nextLevel
		currLevel += 1
	if not success:
		print("Case #" + str(case) + ": IMPOSSIBLE")



	
	#print("Case #" + str(case) + ": " + str(right) + " " + str(left)) # right >= left