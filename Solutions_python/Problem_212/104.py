for test in range(1, int(input()) + 1):
	n, p = map(int, input().split())
	a = list(map(int, input().split()))
	cnt = [0] * p
	for i in a:
		cnt[i % p] += 1
	ans = cnt[0]
	if p == 2:
		ans += cnt[1] // 2
		cnt[1] -= (cnt[1] // 2) * 2
		ans += cnt[1] > 0
	elif p == 3:
		kek = min(cnt[1], cnt[2])
		cnt[1] -= kek
		cnt[2] -= kek
		ans += kek
		ans += cnt[1] // 3
		ans += cnt[2] // 3
		cnt[1] -= (cnt[1] // 3) * 3
		cnt[2] -= (cnt[2] // 3) * 3
		ans += cnt[1] + cnt[2] > 0
	else:
		ans += cnt[2] // 2
		cnt[2] -= (cnt[2] // 2) * 2
		kek = min(cnt[1], cnt[3])
		cnt[1] -= kek
		cnt[3] -= kek
		ans += kek
		if cnt[2] and cnt[1] >= 2:
			ans += 1
			cnt[2] = 0
			cnt[1] -= 2
		if cnt[2] and cnt[3] >= 2:
			ans += 1
			cnt[2] = 0
			cnt[3] -= 2

		ans += cnt[1] // 4
		cnt[1] -= (cnt[1] // 4) * 4
		ans += cnt[3] // 4
		cnt[3] -= (cnt[3] // 4) * 4
		ans += cnt[1] + cnt[2] + cnt[3] > 0
	print("Case #%d: %d" % (test, ans))
