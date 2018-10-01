#! /usr/bin/env python3
T = int(input())
for i in range(1, T+1):
	N, S, p, *totals = map(int, input().split())
	n = 0
	for t in totals:
		# p-1, p-1, p
		if t >= p * 3 - 2:
			n += 1
		# p-2, p-2, p
		elif t < p * 3 - 4:
			pass
		# p-2, p-2, p => p*3-4
		# p-2, p-1, p => p*3-3
		elif S and p >= 2:
			S -= 1
			n += 1
	print('Case #%d: %d' % (i, n))
