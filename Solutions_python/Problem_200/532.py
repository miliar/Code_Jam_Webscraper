import sys

def solve(case):
	print("Case #{}: ".format(case), end='')
	n0, = sys.stdin.readline().split()
	n = list(n0)
	i = 0
	for j in range(1, len(n)):
		if n[j-1] < n[j]:
			i = j
		elif n[j-1] > n[j]:
			break
	else:
		i = -1
	if i != -1:
		n[i] = str(int(n[i]) - 1)
		for j in range(i+1, len(n)):
			n[j] = '9'
	while len(n) > 1 and n[0] == '0':
		n = n[1:]
	print("".join(n))

def main():
	t = int(sys.stdin.readline())
	for i in range(t):
		solve(i+1)

if __name__ == "__main__":
	main()


