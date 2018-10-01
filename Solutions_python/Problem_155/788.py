def analyse(line):
	values = [int(c) for c in line.split(" ")[1]]

	friends = 0
	standing = 0
	for i in range(len(values)):
		if standing < i:
			friends += i - standing
			standing += i - standing
		standing += values[i]

	return str(friends)

def run(name):
	lines = [l for l in open(name + ".in", mode='r')]
	n = int(lines[0])
	
	out = open(name + ".out",mode='w')
	for i, line in enumerate(lines[1:]):
		answer = analyse(line[:-1])
		out.write("Case #" + str(i+1) + ": " + answer + "\n")
		if "test" in name:
			print("Case #" + str(i+1) + ": " + answer)
	out.close()

run("A-large")