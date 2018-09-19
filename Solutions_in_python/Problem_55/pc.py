import sys

C = int(sys.stdin.readline())

for case in range(C):
	line = sys.stdin.readline().split()
	R = int(line[0])
	k = int(line[1])
	N = int(line[2])
	gi = [int(c) for c in sys.stdin.readline().split()]
	if sum(gi) <= k:
		ans = sum(gi) * R
	else:
		gi = gi + gi
		ei = []
		nexti = []
		lastidx = 0
		summ = 0
		for i in range(N):
			for c in gi[lastidx:]:
				if (summ + c) > k:
					break
				else:
					lastidx += 1
					summ += c
			if lastidx >= N:
				nexti.append(lastidx - N)
			else:
				nexti.append(lastidx)
			ei.append(summ)
			summ -= gi[i]

		next_one = nexti[0]
		ri = [ei[0]]
		stepi = N*[-1]
		stepi[0] = 0
		steps = 1
		while (stepi[next_one]==-1):
			ri.append(ei[next_one])
			stepi[next_one] = steps
			steps += 1
			next_one = nexti[next_one]

#		print stepi[next_one]
#		print ri

		round_steps = steps - stepi[next_one]
		round_sum = sum(ri[stepi[next_one]:])
		first_steps = stepi[next_one]
		first_sum = sum(ri[:first_steps])

#		print first_steps
#		print first_sum
#		print round_steps
#		print round_sum
		if R <= first_steps:
			ans = sum(ri[:R])
		else:
			R -= first_steps
			ans = first_sum + (R/round_steps)*round_sum + sum(ri[stepi[next_one]:stepi[next_one]+(R%round_steps)])

	print "Case #%d: %d"%(case+1, ans)
