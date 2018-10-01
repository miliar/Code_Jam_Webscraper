#!/usr/bin/python

def solve(m, n, k):
	ok = False
	a = [ [ "*" for y in range(n) ] for x in range(m) ]
	if k == 1:
		ok = True
		a[0][0] = '.'
	elif m == 1:
		ok = True
		for y in range(n):
			a[0][y] = "." if y < k else "*"
	elif n == 1:
		ok = True
		for x in range(m):
			a[x][0] = "." if x < k else "*"
	elif m == 2:
		if k >= 4 and k % 2 == 0:
			ok = True
			for y in range(n):
				a[0][y] = a[1][y] = "." if y < k / 2 else "*"
	elif n == 2:
		if k >= 4 and k % 2 == 0:
			ok = True
			for x in range(m):
				a[x][0] = a[x][1] = "." if x < k / 2 else "*"
	else:
		for p in range(2, m + 1):
			for q in range(2, n + 1):
				if not ok and 2 * (p + q - 2) <= k and k <= p * q:
					ok = True
					for x in range(p):
						for y in range(q):
							a[x][y] = "." if x < 2 or y < 2 or ((x - 2) * (q - 2) + (y - 2) < k - (2 * (p + q - 2))) else "*"
	if ok:
		a[0][0] = "c"
		return a

for tc in range(1, 1 + int(raw_input())):
	print "Case #{0}:".format(tc)
	m, n, l = [ int(_) for _ in raw_input().split() ]
	k = m * n - l
	# print "{0} {1} {2}".format(m, n, k)
	ans = solve(m, n, k)
	if ans:
		for x in range(m):
			print "".join(ans[x])
	else:
		print "Impossible"
	# print ""

