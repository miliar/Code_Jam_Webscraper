n_test = int(raw_input())

for t in xrange(1, n_test + 1):
	pl_min, len_flipper = raw_input().split()
	pl_min = map(lambda c: 1 if c == '+' else 0, list(str(pl_min)))
	len_flipper = int(len_flipper)

	toggle = [None for _ in xrange(len(pl_min))]
	n_toggle = ctr = 0
	possible = True
	for i, c in enumerate(pl_min):
		toggle[i] = 1 if (c + n_toggle) % 2 == 0 else 0
		n_toggle += toggle[i] - (1 if i >= len_flipper - 1 and toggle[i - len_flipper + 1] == 1 else 0)
		ctr += toggle[i]
		if i > len(pl_min) - len_flipper and toggle[i] == 1:
			possible = False
			break
	if possible:
		print "Case #" + str(t) + ": " + str(ctr)
	else:
		print "Case #" + str(t) + ": " + "IMPOSSIBLE"