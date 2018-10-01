from operator import mul
from functools import reduce

atol = 1e-8
rtol = 1e-5
def isclose(a, b):
	return abs(a-b) <= atol + rtol*b

def prod(arr):
	return reduce(mul, arr, 1)

def main():
	num_tests = int(input())

	for t in range(num_tests):
		solve(t+1)

def solve(case):
	n, k = [int(x) for x in input().split(' ')]
	units = float(input())
	probs = [float(x) for x in input().split(' ')]

	probs.append(1)
	probs.sort()

	while not isclose(probs[0], 1) and not isclose(units, 0):
		k = 1
		while isclose(probs[0], probs[k]):
			k += 1
		diff = probs[k] - probs[0]
		add_amount = min(units/k, diff)

		for i in range(k):
			probs[i] += add_amount

		units -= k * add_amount

	print('Case #{}: {}'.format(case, prod(probs)))

main()