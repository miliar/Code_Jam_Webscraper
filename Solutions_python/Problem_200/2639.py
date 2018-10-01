t = int(input())
outcome = ''
for test in range(t):
	found = False
	i = int(input())
	#tens = 0
	j = i
	while j > 0:
		k = j
		check = list(str(j))
		while k > 0:
			if k % 10 >= k % 100 // 10:
				k //= 10
			else:
				break
			if k < 10:
				outcome = j
				found = True
				break
		for a in range(len(check)-1):
			if check[a] > check[a+1]:
				check[a] = str(int(check[a])-1)
				for b in range(a+1, len(check)):
					check[b] = '9'
		check = int(''.join(check))
		if check >= j:
			j -= 1
		else:
			j = check
		if found: break
	print(f"Case #{test+1}: {outcome}")

