T = int(input())
for i in range(T):
	N = input()
	changed = True
	while changed:
		changed = False
		j = len(N) - 1
		while j > 0:
			if N[j - 1] > N[j]:
				N = str(int(N) - 1)
				changed = True
				break
			j -= 1

	print("Case #{}: {}".format(i + 1, int(''.join(N))))