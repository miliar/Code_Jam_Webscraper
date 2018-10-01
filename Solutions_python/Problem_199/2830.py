def flipInSize(pancake, flipper, indexOfBlank):
	rigthSideOfFlipper = indexOfBlank + flipper
	changes = ""
	for i in xrange(indexOfBlank, rigthSideOfFlipper):
		if pancake[i] == "-":
			changes += "+"
		else:
			changes += "-"
	return pancake[:indexOfBlank] + changes + pancake[rigthSideOfFlipper:]

def flip(pancake, flipper):
	flipCount = 0
	loopLength = len(pancake) - flipper + 1
	for i in xrange(0, loopLength):
		if pancake[i] == "-":
			pancake = flipInSize(pancake, flipper, i)
			flipCount += 1
	if "-" in pancake:
		return "IMPOSSIBLE"
	else:
		return flipCount

t = int(raw_input())
for i in xrange(1, t + 1):
	n = [s for s in raw_input().split(" ")]
	print "Case #{}: {}".format(i, flip(n[0], int(n[1])))