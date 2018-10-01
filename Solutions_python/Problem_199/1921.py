

def verify(stringo):
	return stringo.count('+') == len(stringo)

def toggle(char):
	if char == '+':
		return '-'
	elif char == '-':
		return '+'
	else:
		return '0'

def solution(S, K):
	
	N = len(S)
	K = int(K)
	S = list(S)

	count = 0 

	if verify(S):
		return count

	minuses = S.count('-')
	pluses = S.count('+')

	if minuses % 2 == 1 and K % 2 == 0: # odd number of minuses and K evens, impossible
		return 'IMPOSSIBLE'

	for index in range(0, N - K + 1):
		
		if S[index] == '-':
			count += 1
			S[index:index+K] = [toggle(element) for element in S[index:index+K]]
			
	if verify(S):
		return count
	else:
		return 'IMPOSSIBLE'


T = int(input().strip())

for _ in range(T):
	S, K = input().strip().split(' ')


	print('Case #' + str(_+1) + ':', str(solution(S,K)))
