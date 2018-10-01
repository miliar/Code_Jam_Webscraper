for tt in xrange(1, input() + 1):
	N, P = map(int, raw_input().split())
	cnt = [0 for i in xrange(P)]
	for x in map(int, raw_input().split()):
		cnt[x % P] += 1
	ans = 0
	if P == 2:
		ans = cnt[0] + cnt[1] / 2 + cnt[1] % 2
	if P == 3:
		ans = cnt[0]
		if cnt[1] < cnt[2]:
			ans += cnt[1]
			ans += (cnt[2] - cnt[1]) / 3
			if (cnt[2] - cnt[1]) % 3:
				ans += 1
		if cnt[1] > cnt[2]:
			ans += cnt[2]
			ans += (cnt[1] - cnt[2]) / 3
			if (cnt[1] - cnt[2]) % 3:
				ans += 1
		if cnt[1] == cnt[2]:
			ans += cnt[1]
	print "Case #" + str(tt) + ": " + str(ans)