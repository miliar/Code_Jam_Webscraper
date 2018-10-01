for T in xrange(int(raw_input())):
	d = [int(i) for i in raw_input().split()]
	N = d[0]
	S = d[1]
	p = d[2]
	ans = 0
	maybe = 0
	for i in d[3:]:
		if i >= 3*p - 2:
#			print "yes", i
			ans += 1
		elif i >= 3*p-4:
			if p > 1:
#				print "maybe", i
				maybe += 1
	ans += min(maybe,S)
	print "Case #%d: %d" % (T+1, ans)


#100 -> 1
#p=1
