num_tests = int(input())

results = ['' for i in range(num_tests)]

for i in range(num_tests):

	num_flips = 0

	test, flip_range = input().split()

	pancakes = [True if c is '+' else False for c in test]
	flip_range = int(flip_range)

	for j in range(len(pancakes) - flip_range + 1):
		if pancakes[j] == False:
			for k in range(flip_range):
				pancakes[j + k] = not pancakes[j + k]
			num_flips += 1

	if False in pancakes:
		results[i] = 'Case #{}: IMPOSSIBLE'.format(i + 1)

	else:
		results[i] = 'Case #{}: {}'.format(i + 1, num_flips)

for result in results:
	print(result)
