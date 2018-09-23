def max_fresh_packs(mods):
	p = len(mods)

	ans = mods[0]


	if p == 2:
		ans += mods[1]//2
		if mods[1] % 2 != 0:
			ans += 1

	elif p == 3:
		m = min(mods[1], mods[2])
		ans += m
		mods[1] -= m
		mods[2] -= m
		ans += max(mods[1], mods[2])//3
		if max(mods[1], mods[2]) % 3 != 0:
			ans += 1

	elif p == 4:
		m = min(mods[1], mods[3])
		ans += m
		mods[1] -= m
		mods[3] -= m

		ans += mods[2]//2
	
		if mods[2] % 2 != 0:  # one 2 left over
			if mods[1] != 0:  # we still have 1's left
				mods[1] += 2
			else:
				mods[3] += 2
		
		if mods[1] != 0:  # we still have 1's left
			ans += mods[1] // 4
			if mods[1] % 4 != 0:
				ans += 1
		else:
			ans += mods[3] // 4
			if mods[3] % 4 != 0:
				ans += 1

	return ans






t = int(input())  # read a line with a single integer

for j in range(1, t + 1):
    n, p = map(int, input().split(" "))

    groups = list(map(int, input().split(" ")))

    mods = [0]*p

    for i in groups:
    	mods[i%p] += 1

    print("Case #{}: {}".format(j, max_fresh_packs(mods)))