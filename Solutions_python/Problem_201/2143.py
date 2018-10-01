import fileinput

num = 0;
inputs = [];

for line in fileinput.input():
	if fileinput.isfirstline():
		num = int(line)
	else:
		inputs.append(line.split(" "))

def choose_stall(stalls):
	# Compute values for each stall
	min_lr = []
	max_lr = []

	for s_idx in range(0, len(stalls)):
		if stalls[s_idx] == 1:
			min_lr.append(-1)
			max_lr.append(-1)
		else:
			# Search left
			L = 0
			lidx = s_idx - 1
			while (stalls[lidx] != 1):
				L+=1
				lidx-=1

			R = 0
			ridx = s_idx + 1
			while (stalls[ridx] != 1):
				R+=1
				ridx+=1

			min_lr.append(min(L, R))
			max_lr.append(max(L, R))

			# print(s_idx, L, R)

	# print(min_lr)
	# print(max_lr)

	max_val = max(min_lr)
	picked = [s for s in range(len(stalls)) if min_lr[s] == max_val]

	# print(picked)
	if len(picked) > 1:
		max_val2 = max([max_lr[p] for p in picked])
		# print(max_val2)

		picked = [s for s in picked if max_lr[s] == max_val2]
		# print(picked)

		if len(picked) > 1:
			picked = min(picked)
		else:
			picked = picked[0]
	else:
		picked = picked[0]

	# print(picked)

	# Seat person at chosen seat
	stalls[picked] = 1

	return min_lr, max_lr, picked

def simulate(N, K):

	# Create stalls
	stalls = [0 for i in range(N + 2)]
	# Fill in guards
	stalls[0] = 1
	stalls[-1] = 1
	for p in range(K):
		# Fill in stall where person p sits
		if p == K - 1:
			min_lr, max_lr, s = choose_stall(stalls)
		else:
			min_lr, max_lr, s = choose_stall(stalls)
		# print(stalls)

	return(max_lr[s], min_lr[s])

for idx, case in enumerate(inputs):
	N = int(case[0])
	K = int(case[1])
	y, z = simulate(N, K)
	print("Case #" + str(idx + 1) + ": " + str(y) + " " + str(z))


