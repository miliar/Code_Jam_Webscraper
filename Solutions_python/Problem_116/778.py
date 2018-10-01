import sys
import math
import re

def check(xo, rcd):

	#print (xo, ':', rcd)
	for i in rcd:
		#print (xo, ':', i)
		#print (i.count(xo), '+', i.count('T'))
		if (i.count(xo) + i.count('T') == 4):
			return True
	return False


def case():

	rows = sys.stdin.read(21).split('\n')[:4]
	cols = ['','','','']
	diags = ['','']

	completed = True

	for row in rows:
		for i in range(4):
			if (row[i] == '.'):
				completed = False
			cols[i] += row[i]

	for i in range(4):
		diags[0] += rows[i][i]

	for i in range(4):
		diags[1] += rows[i][3-i]

	#print (rows)
	#print (cols)
	#print (diags)

	if (check('X', rows) or check('X', cols) or check('X', diags)):
		sys.stdout.write('X won')
	elif (check('O', rows) or check('O', cols) or check('O', diags)):
		sys.stdout.write('O won')
	elif completed:
		sys.stdout.write('Draw')
	else:
		sys.stdout.write('Game has not completed')



if __name__=="__main__":

	if len(sys.argv) > 1:
		sys.stdin = open(sys.argv[1])

	num_cases = int(input())

	for c in range (1, num_cases+1):
		sys.stdout.write('Case #')
		sys.stdout.write(str(c))
		sys.stdout.write(': ')
		case()
		sys.stdout.write('\n')
