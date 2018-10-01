

def readInput(testfile):
	with open(testfile, 'rb') as f:
		lines = list()
		for line in f:
			lines.append(line)
	return lines

def readTestCase(input_lines):
	first_answer = int(input_lines[0].strip())
	first_grid = ([[int(number) for number in line.strip().split(" ")] for line in input_lines[1:5]])
	second_answer = int(input_lines[5].strip())
	second_grid = ([[int(number) for number in line.strip().split(" ")] for line in input_lines[6:10]])
	return first_answer, first_grid, second_answer, second_grid

def writeAnswerOutputs(output_lines):
	with open("answer.txt", 'wb') as f:
		f.write("\n".join(output_lines))

if __name__ == "__main__":
	lines = readInput("A-small-attempt0.in")
	test_cases = int(lines[0].strip())
	cases = []
	for i in xrange(0,test_cases):
		first_answer, first_grid, second_answer, second_grid = readTestCase(lines[i * 10 + 1: i * 10 + 11])
		# print "answer was {0}, for grid:\n{1}".format(first_answer, first_grid)
		first_possible = first_grid[first_answer - 1]
		second_possible = second_grid[second_answer - 1]
		possible =  [guess for guess in second_possible if guess in first_possible]

		determine = len(possible)
		if determine == 1:
			answer = str(possible[0])
		elif determine == 0:
			answer = "Volunteer cheated!"
		else:
			answer = "Bad magician!"
		cases.append("Case #%d: %s" % (i + 1, answer))
	writeAnswerOutputs(cases)
	print "Done"