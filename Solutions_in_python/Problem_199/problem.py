#skleton
T = int(input())
for t in range(T):
	result = 0
	line = input().split(' ')
	pancake = ','.join(line[0]).split(',')
	K = int(line[1])

	for idx in range(len(pancake)-K+1):
		if(pancake[idx] == '+'):
			continue
		else:
			for i in range(K):
				if(pancake[idx+i] == '-'):
					pancake[idx+i] = '+'
				else:
					pancake[idx+i] = '-'
			result += 1
	if(pancake == ['+']*len(pancake)):
		print("Case #{0}: {1}".format(t+1, result))
	else:
		print("Case #{0}: {1}".format(t+1, "IMPOSSIBLE"))