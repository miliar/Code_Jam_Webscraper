import sys	


flip = {'+': '-', '-': '+'}


def flip_pancakes(S, K):
	if '-' not in S:
		return 0

	i = 0
	n_flips = 0
	while i < len(S) - K + 1:
		if S[i] == '-':
			new_S = S[:i]
			n_flips += 1
			for j in range(i, i + K):
				new_S += flip[S[j]]
			if j + 1 < len(S):
				new_S += S[j+1:]
			S = new_S
		i += 1

	if '-' in S:
		return 'IMPOSSIBLE'
	else:
		return n_flips

def solve_case(case, f, fout):
	S, K = f.readline().strip().split()
	K = int(K)
	result = flip_pancakes(S, K)
	write_line(fout, case, str(result))

def write_line(fout, n, result):
	print("Case #%d: %s\n" %(n, result))
	fout.write("Case #%d: %s\n" %(n, result))

if __name__ == '__main__':
	
	input_file_name = sys.argv[1]
	
	f = file(input_file_name)
	fout = file("%s.out" %(input_file_name.split(".")[0]), "w")
	
	T = eval(f.readline())
	
	for case in xrange(T):
		solve_case(case + 1, f, fout)
		
	f.close()
	fout.close()
