import os


def readLines(filename):
	input = open(filename, 'rb')
	lines = []
	for line in input:
		line = line.replace('\n','')
		lines.append(line)	
	input.close()
	return lines

def writeLines(output):
	outputFile = open('output.txt', 'w')
	for line in output:
		outputFile.write(line + '\n')
	outputFile.close()

def solveProblem(line):
	args = line.split(' ')
	space = int(args[0])
	target_index = int(args[1])
	nodes = 1
	prev_nodes = 0
	while True:
		space -= nodes
		value, remain = divmod(space, nodes * 2)
		if prev_nodes < target_index <= prev_nodes + nodes:
			target_i = target_index - prev_nodes
			if remain > nodes and target_i <= remain - nodes:
				return '{0} {1}'.format(value + 1, value + 1)
			elif target_i <= remain:
				return '{0} {1}'.format(value + 1, value)
			else:
				return '{0} {1}'.format(value, value)
		prev_nodes += nodes
		nodes *= 2


lines = readLines('input.txt')
total = int(lines[0])
output = []
for i in range(1, total+1):
	value = solveProblem(lines[i])
	line = 'Case #{0}: {1}'.format(i, value)
	output.append(line)
writeLines(output)
