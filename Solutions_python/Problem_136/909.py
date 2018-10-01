T = input()
for cas in xrange(1, T+1):
	C, F, X = map(float, raw_input().split())
	add = 0
	ans = []
	x = 0
	while 1:
		tot = add+X/(2+F*x)
		ans.append(tot)
		if len(ans) > 1 and tot > ans[len(ans)-2]:
			break
		add += C/(2+F*x)
		x += 1
	# print len(ans)
	# print ans
	print 'Case #'+str(cas)+': '+str(ans[::-1][1])
