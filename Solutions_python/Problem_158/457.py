import math


def solve(ominoes, width, height):

	if (width * height) % ominoes == 0:
		sqrt = math.sqrt(ominoes)
		if (ominoes == 4) and ((width == 2 and height == 4) or (width == 4 and height == 2)):
			print ominoes, width, height
			return "RICHARD"
		if (ominoes > 2 and (sqrt > width or sqrt > height)) or (ominoes > width and ominoes > height):
			print ominoes, width, height
			return "RICHARD"
		else:
			print ominoes, width, height
			return "GABRIEL"
	else:
		print ominoes, width, height
		return "RICHARD"


name = "D-small-attempt2"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split(" ")
	line = map(int, line)

	fout.write("Case #" + str(i + 1) + ": " + solve(line[0], line[1], line[2]) + "\n")
	print "Case #" + str(i + 1) + ": " + solve(line[0], line[1], line[2])

fi.close()
fout.close()