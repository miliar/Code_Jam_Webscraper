import sys

def solve(S_max, S_str):
	y = 0
	n = int(S_str[0])
	for i in range(1,S_max+1):
		d = int(S_str[i])
		if n < i:
			y+=(i-n)
			n+=(i-n)
		n+=d

	return y


def io(filename):
	output = open(filename.split('.')[0]+'.out', 'w')
	with open(filename, 'r') as f:
		T = int(f.readline())
		for t in range(T):
			S_max, S_str = f.readline().split()
			output.write("Case #{x}: {y}\n".format(x=t+1, y=solve(int(S_max), S_str)))
			

if __name__ == '__main__':
	input_file = sys.argv[1]
	io(input_file)