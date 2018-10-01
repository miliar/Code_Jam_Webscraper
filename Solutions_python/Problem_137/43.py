import sys
tt = int(raw_input())
for t in xrange(1, tt + 1):
	print "Case #" + str(t) + ":"
	r, c, m = map(int, raw_input().split())
	s = r * c - m
	if s == 1:
		print "c" + "*" * (c - 1)
		sys.stdout.write(("*" * c + "\n") * (r - 1))
		continue
	if r == 1:
		print "c" + "." * (c - m - 1) + "*" * m
		continue
	if c == 1:
		sys.stdout.write("c\n" + ".\n" * (r - m - 1) + "*\n" * m)
		continue
	if r == 2:
		if m % 2 == 1 or s < 4:
			print "Impossible"
		else:
			print "c" + "." * (c - m / 2 - 1) + "*" * (m / 2)
			print "." * (c - m / 2) + "*" * (m / 2)
		continue
	if c == 2:
		if m % 2 == 1 or s < 4:
			print "Impossible"
		else:
			print "c."
			sys.stdout.write("..\n" * (s / 2 - 1))
			sys.stdout.write("**\n" * (m / 2))
		continue
	if s < 4 or s == 5 or s == 7:
		print "Impossible"
		continue
	if s == 4:
		print "c." + "*" * (c - 2)
		print ".." + "*" * (c - 2)
		sys.stdout.write(("*" * c + "\n") * (r - 2))
		continue
	if s <= 3 * c:
		q1 = s / 3 - 1 if s % 3 == 1 else s / 3
		q2 = (s + 2) / 3
		print "c" + "." * (q2 - 1) + "*" * (c - q2)
		print "." * q2 + "*" * (c - q2)
		print "." * q1 + "*" * (c - q1)
		sys.stdout.write(("*" * c + "\n") * (r - 3))
	else:
		print "c" + "." * (c - 1)
		sys.stdout.write(("." * c + "\n") * (s / c - 2))
		print "." * (c - 1) + ("*" if s % c == 1 else ".")
		if s % c != 0:
			print "." * max(2, s % c) + "*" * (c - max(2, s % c))
		sys.stdout.write(("*" * c + "\n") * (r - (s + c - 1) / c))