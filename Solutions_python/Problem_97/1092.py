def compute(data):
	[A, B] = [int(d) for d in data]
	y = 0
	cache = []
	for n in range(A, B + 1):
		sn = str(n)
		l = len(sn)
		for i in range(1, l):
			if sn[-i] != '0':
				sm = sn[-i:] + sn[:(l - i)]
				m = int(sm)
				if A <= n < m <= B and [n, m] not in cache:
					y += 1
					cache += [[n, m]]
	return y

def solve(input):
	data = input.split('\n')
	T = int(data.pop(0))
	data = data[0:T]
	output = ''
	for x in range(len(data)):
		#######
		y = compute(data[x].split(' '))
		#######
		output += 'Case #%d: %d' % (x + 1, y) + '\n'
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