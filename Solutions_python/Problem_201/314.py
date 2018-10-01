# Read file and parse

filename = "C-large"
infile= filename + '.in'
f = open(infile)
inp = f.read().splitlines()
f.close()
outfile = filename + '.out'
f = open(outfile,'w')
case = int(inp.pop(0))

# Solve here
def Solve(num):
	N,K = num.split()
	N = int(N)
	K = int(K)
	res = [0,0]
	Ava={N:1}
	i = 0
	times = 0
	while i < K:
		cand = max(Ava)
		times = Ava[cand]
		del Ava[cand]
		if cand % 2 == 0:
			res[0] = cand//2
			res[1] = res[0]-1
		else:
			res[0] = res[1] = (cand-1) // 2
		if res[0] in Ava:
			Ava[res[0]] += times
		else:
			Ava[res[0]] = times
		if res[1] in Ava:
			Ava[res[1]] += times
		else:			
			Ava[res[1]] = times
		i += times	
	return res

# Output
for case in range(1, case + 1):
	result = Solve(inp[case-1])
	print('Case #{}: {} {}'.format(case, result[0], result[1]))
	f.write('Case #{}: {} {}\n'.format(case, result[0], result[1]))
f.close()	
