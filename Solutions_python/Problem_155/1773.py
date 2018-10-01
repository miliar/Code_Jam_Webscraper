t = int(input())
for tt in range(1,t+1):
	n, shyness = input().split()
	ans, up = 0, 0
	for i, s in enumerate(shyness):
		if up >= i:
			up += int(s)
		else:
			diff = i - up
			up += diff + int(s)
			ans += diff

	print('Case #{}: {}'.format(tt, ans))