import math
import itertools

def solve(case):
	count = 0
	
	case = case.split(' ')
	low = math.ceil(int(case[0])**0.5)
	high = math.floor(int(case[1])**0.5)
	
	psqrts = open('s.txt','r')
	psqrts = psqrts.read().strip().split(', ')
	
	for i in range(len(psqrts)):
		psqrts[i] = int(psqrts[i])
	
	for i in psqrts:
		if i >= low and i <= high:
			count += 1
	
	return str(count)
	
file = open('C-large-1.in','r')
lines = file.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].strip()
file.close()

linesout = []
toout = ''
line = 1
while line < int(lines[0])+1:
	toout = solve(lines[line])
	linesout.append('Case #' + str(len(linesout) + 1) + ': ' + toout + '\n')
	toout = ''
	line = line+1

linesout[-1] = linesout[-1][:-1]
file = open('out','w')
file.writelines(linesout)