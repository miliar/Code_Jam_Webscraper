t = int(raw_input())
for i in range(1, t + 1):
	x, r, c = [int(y) for y in raw_input().split()]
	ans = "RICHARD"
	if r % x == 0 or c % x == 0:
		if max([x - r, x - c]) <= 1:
			ans = "GABRIEL"
		
	print "Case #" + str(i) + ": " + ans


