#!/usr/bin/env python

nmax = 1005

ddd = 1000000000000

t = input()

for ti in range(1, t+1):
	n = input()
	a = map(int, raw_input().split())
	order = sorted(a)

	pos = dict((v, i) for i, v in enumerate(a))
	#print pos

	gr_l = dict((i, 0) for i in range(n))
	gr_r = dict((i, 0) for i in range(n))
	for i in range(n):
		for j in range(i):
			gr_l[i] += 1 if a[j] > a[i] else 0
		for j in range(i+1, n):
			gr_r[i] += 1 if a[j] > a[i] else 0

	#print gr_l
	#print gr_r

	dp = {}
	dp[(0,0)] = 0

	for k in range(1, n+1):
		#print 'k=', k
		current = a[k-1]
		for j in range(k+1):
			l, r = j, k-j
			#print l, r

			val_1, val_2 = None, None
			pos_1 = max(0, l-1), r
			if pos_1 in dp:
				# move to left
				val_1 = dp[(max(0, l-1), r)] + gr_l[pos[current]]
			pos_2 = l, max(0, r-1)
			if pos_2 in dp:
				val_2 = dp[(l, max(0, r-1))] + gr_r[pos[current]]

			#print val_1, val_2
			dp[(l, r)] = min(val_1 if val_1 is not None else ddd, val_2 if val_2 is not None else ddd)

	#print dp
	ans = dp[(n, 0)]
	for j in range(n):
		ans = min(ans, dp[(j, n-j)])
	print 'Case #' + str(ti) + ':', ans