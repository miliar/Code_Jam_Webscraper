import sys
import itertools


possible_x = [1, 2, 3, 4]

possible_r = [1, 2, 3, 4]
possible_c = [1, 2, 3, 4]


possible_tuples = [(x, r, c) for x in possible_x for r in possible_r for c in possible_c if r >= c]
possible_tuples = [(x, r, c) for (x, r, c) in possible_tuples if (r*c) % x == 0]
possible_tuples = [(x, r, c) for (x, r, c) in possible_tuples if x <= max(r, c)]
possible_tuples = [(x, r, c) for (x, r, c) in possible_tuples if not (x > 2 and min(r, c) < 2)]

# Hand-picked
possible_tuples.remove((4, 4, 2))

num_cases = sys.stdin.readline()
num_cases = int(num_cases)

for i in range(1, num_cases + 1):
	line = sys.stdin.readline()
	x, r, c = map(int, line.split())
	if c > r:
		r, c = c, r

	answer = (x, r, c) in possible_tuples
	print 'Case #%d: %s' % (i, 'GABRIEL' if answer else 'RICHARD')
