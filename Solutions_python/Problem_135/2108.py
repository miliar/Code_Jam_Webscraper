cases = int(input())

for case in range(1, cases + 1):
	# first
	answer = int(input())
	possible = []
	for row in range(1, 5):
		line = [int(i) for i in input().split(' ')]
		if row == answer:
			possible = line

	# second
	answer = int(input())
	result = []
	for row in range(1, 5):
		line = [int(i) for i in input().split(' ')]
		if row == answer:
			for i in line:
				if i in possible:
					result.append(i)

	out = 'Volunteer cheated!'
	if len(result) > 1:
		out = 'Bad magician!'
	elif len(result) == 1:
		out = result[0]
	print('Case #{}: {}'.format(case, out))
