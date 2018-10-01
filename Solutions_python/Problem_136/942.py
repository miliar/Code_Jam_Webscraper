import sys

test_count = int(sys.stdin.readline())

for test_id in range(1, test_count + 1):
	C, F, X = tuple(map(float, sys.stdin.readline().strip().split(' ')))
	production = 2.0
	acc_time = 0.0
	costs = [X / production]
	while True:
		acc_time += (C / production)
		production += F
		costs.append(acc_time + X / production)
		if costs[-1] > costs[-2]: break
	print('Case #%d: %.7f' % (test_id, costs[-2]))
