import pdb
import sys

def task(inFile):
	X, R, C = [int(n) for n in list(next(inFile)) if n != ' ' and n != '\n']
	if (R*C)%X != 0:
		return 'RICHARD'
	else:
		if X > R and X > C:
			return 'RICHARD'

		p1 = X
		p2 = 1
		while p1 > p2:
			p1 = p1 -1
			p2 = p2 + 1

		if (p1 > R and p2 > R) or (p1 > C and p2 > C):
			return 'RICHARD'

		elif X > 3 and ((p1 >= R and p2 >=R ) or (p1 >= C and p2 >= C)):
			return 'RICHARD'
		else: return 'GABRIEL'

output = open('output.txt',  mode='w', encoding='utf-8')

with open(sys.argv[1], encoding='utf-8') as inFile:
	T = int(next(inFile))

	for t in range(0,T):
		output.write('Case #{0}: {1}\n'.format(t+1, task(inFile )))