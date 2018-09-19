input = open('A-small.in')
output = open('output.out', 'w+')

def func(line):
	counter = 0
	audSum = 0
	for index, val in enumerate(line):
		if int(val) != 0:
			if index > audSum:
				counter += index - audSum
				audSum += counter
				audSum += int(val)
			else:
				audSum += int(val)
	return counter

numOfCases = ...
maxShyLevel = ...
levelMask = ...

numOfCases = int(input.readline()[:-1])

i = 1
for line in input.readlines():
	output.write('Case #'+ str(i) + ': ' + str(func(line.split(' ')[1][:-1])) + '\n')
	i += 1



