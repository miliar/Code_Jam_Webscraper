from __future__ import division

import sys
import math

output = []

f = open(sys.argv[1])
try:
	for N in range(1, int(f.next()) + 1):
		P, K, L = map(int, f.next().split())
		
		letters = sorted(map(int, f.next().split()))
		letters.reverse()
		
		n = 0
		for i, let in enumerate(letters):
			n += let * math.ceil((i + 1) / K)
		output.append((N, int(n)))
finally:
	f.close()

f = open(sys.argv[2], 'w')
try:
	f.write('\n'.join('Case #%s: %s' % o for o in output))
finally:
	f.close()