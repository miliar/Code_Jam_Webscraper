fileIn = 'A-large.in'
fileOut = 'output.txt'

f = open(fileOut, 'w')

def count(line):
	p = 0
	if len(line) == 0: return p

	for i in range(1,len(line)):
		if line[i] and sum(line[:i]) < i:
			add = i - sum(line[:i])
			p += add
			line[0] += add
	return p

lines = []
samples = None;
case = 1;
with open(fileIn, 'r') as f1: 
	for line in f1:
		if not samples:
			samples = [int(x) for x in line.split()]
		else:
			lines = line.split()
			lines = [int(x) for x in list(lines[1])]
			f.write("Case #" + str(case) + ": "+ str(count(lines)) + "\n")
			lines = []
			case += 1




f.close()
