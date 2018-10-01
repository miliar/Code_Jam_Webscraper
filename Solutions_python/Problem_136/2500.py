def calculate(c, f, x):
	rate = 2
	timeSpentOnFarms = 0

	while True:
		time = timeSpentOnFarms + x / rate
		timeSpentOnFarms += c / rate
		rate += f
		if time <= timeSpentOnFarms + x / rate:
			break;

	return time

output = open("output.txt", "w")
lineNumber = 0
for line in open("B-large.in"):
	lineNumber += 1

	if lineNumber == 1:
		continue;

	c, f, x = map(lambda x: float(x.strip()), line.split(" "))
	result = calculate(c, f, x)
	output.write("Case #%s: %s\n" % (lineNumber - 1, result))