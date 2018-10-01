T = int(input())


for t in range(T):
	Ac, Aj = [int(i) for i in input().split()]

	if Ac == Aj and Ac == 1: # Ac1 Aj1
		Cc, Dc = [int(i) for i in input().split()]
		Cj, Dj = [int(i) for i in input().split()]
		print("Case #{}: ".format(t+1) + "2")

	elif Ac == 2 or Aj == 2: # Ac2 Aj0 or Ac0 Aj2
		C1, D1 = [int(i) for i in input().split()]
		C2, D2 = [int(i) for i in input().split()]
		diff1 = D2 - C1
		diff2 = D1 - C2
		if diff1 < 0: diff1 += 1440
		if diff2 < 0: diff2 += 1440
		diff = min(diff1, diff2)
		if diff <= 720:
			print("Case #{}: ".format(t+1) + "2")
		else:
			print("Case #{}: ".format(t+1) + "4")

	else: # Ac1 Aj0 ro Ac0 Aj1
		C, D = [int(i) for i in input().split()]
		print("Case #{}: ".format(t+1) + "2")


