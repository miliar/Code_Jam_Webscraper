import sys

def solve(S, K):

	N = len(S)

	def flip(s, n):
		for i in range(K):
			if s[n+i] == '+':
				s[n+i] = '-'
			elif s[n+i] == '-':
				s[n+i] = '+'
			else:
				raise Exception('flip: illegal character in s')

	# def print_out(s):
	# 	print ''.join(s)
		
	num_flips = 0
	# print_out(S)
	for n in range(N-K+1):
		if S[n] == '-':
			flip(S, n)
			num_flips += 1
			# print_out(S)
	result = num_flips if '-' not in S else 'IMPOSSIBLE'
	# print 'num_flips: {}'.format(result)
	return result

lines = sys.stdin.readlines()

T = int(lines[0].strip())

for t in range(T):
	S, K = lines[t+1].strip().split()
	S = list(S)
	K = int(K)
	answer = solve(S, K)
	print "Case #{}: {}".format(t+1, answer)
