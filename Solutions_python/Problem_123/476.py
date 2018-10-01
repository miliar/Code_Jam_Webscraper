import sys
f = sys.stdin
T = int(f.readline())
for tc in xrange(1, T + 1):
	A, N = [int(x) for x in f.readline().rstrip('\r\n').split()]
	motes = sorted([int(x) for x in f.readline().rstrip('\r\n').split()])
	i = 0
	op = 0
	while i < len(motes):
		# print "A ", A, " mote ", motes[i], " op ", op, " i ", i
		if A > motes[i]:
			A += motes[i]
			i += 1
		else:
			num_ajout = 0
			temp_a = A
			if temp_a != 1:
				while num_ajout < len(motes) - i:
					temp_a += temp_a - 1
					num_ajout += 1
					if  temp_a > motes[i]:
						break
				if num_ajout < len(motes) - i and temp_a > motes[i]:
					op += num_ajout
					# i += 1
					# print 'ajout de ', temp_a, ' a ', A, ' ', num_ajout, ' ajouts'
					A = temp_a # + motes[i]
				else:
					op += len(motes) - i
					i = len(motes)
			else:
				op += len(motes) - i
				i = len(motes)
		if op > len(motes):
			op = len(motes)
			i = len(motes)
	print 'Case #{tc}: {op}'.format(tc=tc, op=op)