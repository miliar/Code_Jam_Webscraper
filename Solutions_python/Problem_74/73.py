import psyco
import math
import sys

INPUT_FILENAME = "A-large"

sample = file("%s.in" % INPUT_FILENAME, "rb")
output = file("%s.out" % INPUT_FILENAME, "wb")

psyco.full()

def toOutput(line):
	print line
	output.write("%s\n" % line)

def solve(caseNumber, orange, blue, steps):
	t = 0
	oPos = 1
	bPos = 1

	while steps:
		oPressed = False
		t += 1

		if orange:
			if oPos != orange[0]:
				if oPos < orange[0]:
					oPos += 1
				else:
					oPos -= 1
			elif steps[0] == "O%d" % oPos:
				orange = orange[1:]
				steps = steps[1:]
				oPressed = True

		if blue:
			if bPos != blue[0]:
				if bPos < blue[0]:
					bPos += 1
				else:
					bPos -= 1
			elif not oPressed and steps[0] == "B%d" % bPos:
				blue = blue[1:]
				steps = steps[1:]

	toOutput("Case #%d: %d" % (caseNumber, t))

numberOfTestCases = int(sample.readline())
for i in xrange(1, numberOfTestCases + 1):
	buttons = sample.readline().strip().split(" ")[1:]
	blue = []
	orange = []
	steps = []

	for j in xrange(0, len(buttons), 2):
		if buttons[j] == "O":
			orange.append(int(buttons[j + 1]))
			steps.append(buttons[j] + buttons[j + 1])
		else:
			blue.append(int(buttons[j + 1]))
			steps.append(buttons[j] + buttons[j + 1])
		
	solve(i, orange, blue, steps)