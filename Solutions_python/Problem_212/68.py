for t in range(1, int(input()) + 1):
	N, P = map(int, input().split())
	gs = [x % P for x in map(int, input().split())]
	n0 = sum(1 for x in gs if x == 0)
	n1 = sum(1 for x in gs if x == 1)
	n2 = sum(1 for x in gs if x == 2)
	n3 = sum(1 for x in gs if x == 3)
	ans = n0 + 1
	if P == 2:
		ans += n1 // 2

	elif P == 3:
		mn12 = min(n1, n2)
		ans += mn12
		n1 -= mn12
		n2 -= mn12
		ans += n1 // 3
		ans += n2 // 3

	elif P == 4:
		mn13 = min(n1, n3)
		ans += mn13
		n1 -= mn13
		n3 -= mn13

		ans += n2 // 2
		n2 %= 2

		if n2 == 1:
			if n1 >= 2:
				n1 -= 2
				n2 -= 1
				ans += 1
			elif n3 >= 2:
				n3 -= 2
				n2 -= 1
				ans += 1
		ans += n1 // 4
		ans += n3 // 4

	if sum(gs) % P == 0:
		ans -= 1
	print('Case #%d: %d' % (t, ans))
