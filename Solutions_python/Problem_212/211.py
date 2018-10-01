#! /usr/bin/python

T = int(raw_input())

for t in range(1, T+1):

	N, P = [int(inp) for inp in raw_input().split()]
	G = [int(inp) for inp in raw_input().split()]

	counts = [0 for _ in range(P)]
	for g in G:
		counts[g % P] += 1

	if P == 2:
		ans = counts[0] + counts[1]/2 + (sum(G) % P != 0)
	elif P == 3:
		cMin = min(counts[1], counts[2])
		cMax = max(counts[1], counts[2])
		ans = counts[0] + cMin + (cMax - cMin)/3 + (sum(G) % P != 0)
	elif P == 4:
		cMin = min(counts[1], counts[3])
		cLeft = max(counts[1], counts[3]) - cMin
		cMid = counts[2] % 2
		cComb = (cMin >= 1 and cLeft >= 2)
		cLeft -= 2*cComb
		ans = counts[0] + counts[2]/2 + cMin + cComb + cLeft/3 + (sum(G) % P != 0)
	else:
		ans = 'incorrect input'

	print 'Case #' + str(t) + ': ' + str(ans)