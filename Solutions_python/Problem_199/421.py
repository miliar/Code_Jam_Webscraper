def import_file(file):
	with open(file) as data:
		T = int(data.readline().rstrip('\n'))
		tests = []
		for datum in data:
			toks = datum.rstrip('\n').split()
			tests.append((toks[0], toks[1]))
	return (T, tests)

def flip(pancakes, n, k):
	# Flips n, n + 1, ... , n + k - 1
	cakes = pancakes[:n]
	cakes.extend(['+' if c == '-' else '-' for c in pancakes[n:n + k]])
	cakes.extend(pancakes[n+k:])

	return cakes

def pancake_flip(pancakes, K):
	curr_pancakes = pancakes
	flips = 0
	for idx in range(len(pancakes) - K + 1):
		if curr_pancakes[idx] == '-':
			curr_pancakes = flip(curr_pancakes, idx, K)
			flips += 1

	if curr_pancakes.count('-') == 0:
		return flips
	else:
		return 'IMPOSSIBLE'

(T, test_cases) = import_file('test.in')
for idx in range(len(test_cases)):
	test = test_cases[idx]
	print('Case #' + str(idx + 1) + ': '),
	print(pancake_flip(list(test[0]), int(test[1])))
