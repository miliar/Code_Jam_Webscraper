import sys

def readinput(filename, func):
	i = -1
	with open(filename) as f:
		for line in f:
			i += 1

			if i == 0:
				cases = int(line.strip())
				continue
				
			if i > cases:
				break

			func(i, *line.split())

def solve(case, smax, si):
	s = [int(si[i]) or 0 for i in range(0, int(smax) + 1)]
	
	clapping = 0
	extra = 0
	for rnd in range(0, int(smax) + 1):
		add = max(0, rnd-clapping)
			
		extra += add
		s[rnd-1] += add
		clapping += s[rnd] + add

	print("Case #{}: {}".format(case, extra))

if __name__ == '__main__':
	try:
		input_file = sys.argv[1]
	except:
		input_file = 'test.in'
	
	readinput(input_file, solve)
