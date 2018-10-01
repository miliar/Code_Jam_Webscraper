for t in range(int(input())):
	n, p = (int(i) for i in input().split())
	a = [0] * p
	for v in input().split():
		i = int(v)
		a[i % p] += 1
	if p == 2:
		res = a[0]
		res += a[1] // 2
		if a[1] % 2 != 0:
			res += 1
	elif p == 3:
		res = a[0]
		pair = min(a[1], a[2])
		res += pair
		rem = a[1] + a[2] - pair * 2
		res += rem // 3
		if rem % 3 != 0:
			res += 1
	else:
		res = a[0]
		pair = min(a[1], a[3])
		res += pair
		rem = a[1] + a[3] - pair * 2
		res += a[2] // 2
		if a[2] % 2 != 0 and rem >= 2:
			res += 1
			rem -= 2
		res += rem // 4
		if rem % 4 != 0:
			res += 1
	print("Case #%d: %d" % (t + 1, res))