import math
from operator import mul

def compute(*args):
	[A, B] = [int(d) for d in args[0]]
	p = [float(d) for d in args[1]]
	E = []
	
	ks_keep  = B - A + 1
	ks_need = B + 1
	
	for i in range(A):
		prob = reduce(mul, p[0:(A-i)])
		ks = 2 * i + ks_keep
		E += [ks * prob + (ks + ks_need) * (1 - prob)]
	
	E += [2 * A + ks_keep]
	E += [1 + ks_need]
	
	y = min(E)
	
	return y

def solve(input):
	data = input.split('\n')
	T = int(data.pop(0))
	data = data[0:T*2]
	output = ''
	for x in range(T):
		#######
		y = compute(data[x*2].split(' '), data[x*2+1].split(' '))
		#######
		output += 'Case #%d: %f' % (x + 1, y) + '\n'
	return output

import sys
if len(sys.argv) > 1:
	with open(sys.argv[1]) as f:
		input = f.read()
	output = solve(input)
	print output
	if len(sys.argv) > 2:
		with open(sys.argv[2], 'w') as f:
			f.write(output)