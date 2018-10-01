T = int(input(""))
case = 1

for cases in range(T):
	j = 0
	cnt = 0
	string = str(input(""))
	S, K = string.split()
	K = int(K)
	S = str(S)
	s = list(S)
	for i in s:
		if(i == '-' and j+K < len(S) + 1):
			cnt += 1
			for k in range(j, j+K):
				if(s[k] == '-'):
					s[k] = '+'
				else:
					s[k] = '-'
		j += 1
	if("-" in s):
		print('Case #{}: {}'.format(case, 'IMPOSSIBLE'))
	else:
		print('Case #{}: {}'.format(case, cnt))
	case += 1