cases = int(input())

for case in range(1, cases + 1):
	C, F, X = [float(i) for i in input().split(' ')]

	rate = 2
	time = 0.0

	while True:
		time_needed = X / rate
		time_for_farm = C / rate

		new_rate = rate + F
		new_time_needed = time_for_farm + X / new_rate

		if new_time_needed < time_needed:
			time += time_for_farm
			rate += F
		else:
			time += time_needed
			break

	print('Case #{}: {}'.format(case, time))
