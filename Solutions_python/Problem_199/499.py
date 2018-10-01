import sys

def solve(s, k, T):
	p = [(c == '+') for c in s]
	n = 0
	for i in range(0, len(p) - k + 1):
		if not p[i]:
			p[i:i+k] = map(lambda x: not x, p[i:i+k])
			n += 1
	for i in range(len(p) - k + 1, len(p)):
		if not p[i]:
			return 'Case #%d: IMPOSSIBLE' % T
	return 'Case #%d: %d' % (T, n)

def run(text):
	idata = text.split('\n')
	T = int(idata[0].strip())
	print T
	output = open('result.out', 'w')
	for t in range(1, T+1):
		s, k = idata[t].strip().split()
		res = solve(s, int(k), t)
		print res
		output.write(res)
		output.write('\n')
	output.close()

if __name__ == '__main__':
	if len(sys.argv) < 2:
		quit()
	
	fname = sys.argv[1]
	with open(fname) as f:
		data = f.read()
	
	run(data)