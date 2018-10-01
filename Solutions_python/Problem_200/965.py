N = int(input())

for T in range(1, N+1):
	n = int(input())
	sn = str(n)

	l = '0'
	d = 0
	j = 0
	for i, c in enumerate(sn):
		if int(c) < int(l):
			#print(sn[:j], int(l)-1, d)
			number = sn[:j]
			if not (int(l) == 1 and j == 0):
				number += str(int(l)-1)

			number += '9' * (len(sn) - j - 1)

			print("Case #%s: %s" % (T, number))
			break

		if c != l:
			d = 1
			j = i
		else:
			d += 1

		l = c
	else:
		print("Case #%s: %s" % (T, sn))

