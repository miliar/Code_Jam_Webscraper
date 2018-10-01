def formatLine(line):
	s = line.split()

	return s

def solveTestCase(line):
	line = formatLine(line)
	line = line[1]

	audience_added = 0
	audience_sum = 0
	for idx, val in enumerate(line):
		if audience_sum < idx:
			audience_sum += 1
			audience_added += 1

		audience_sum += int(val)

	return audience_added


data = open("testfile.txt", 'r')
out = open("answer.txt", "w")
numberCases = int(data.readline())

for i in range(numberCases):
	s = "Case #{0:d}: {1:d}\n".format(i+1, solveTestCase(data.readline()))
	print s
	out.write(s)







		
