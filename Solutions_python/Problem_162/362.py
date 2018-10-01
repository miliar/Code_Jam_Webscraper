# Task А
import fileinput
import sys
sys.setrecursionlimit(10000)

def t(N):
	return int(''.join(reversed(str(N))))

def solve(N):
	if N == 1:
		return 1
	elif N < 19:
		return solve(N - 1) + 1		
	else:
		if N % (10 ** round(len(str(N)) / 2)) == 1:
			tN = t(N)
			if tN < N:
				return solve(tN) + 1
		return solve(N - 1) + 1

stdin = fileinput.input()
T = int(stdin.readline())
for ti in range(T):
	N = int(stdin.readline())
	print('Case #{0}: {1}'.format(ti+1, solve(N)))
