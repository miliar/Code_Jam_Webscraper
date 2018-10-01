import sys

for i in range(0, int(sys.stdin.readline())):
	inputs = sys.stdin.readline()[:-1].split(" ")
	n = int(inputs[0])
	k = int(inputs[1])
	
	stalls = [True] + ([False] * n) + [True]
	while k > 0:
		lsl = []
		rsl = []
		for l in range(1, n + 1):
			ls = 0
			j = l - 1
			while not stalls[j]:
				ls += 1
				j -= 1
			
			rs = 0
			j = l + 1
			while not stalls[j]:
				rs += 1
				j += 1
			
			lsl.append(ls)
			rsl.append(rs)
		
		new_stall = 0
		stall_min = -1
		stall_max = -1
		for l in range(0, n):
			if stalls[l + 1]:
				continue
			
			min_val = min(lsl[l], rsl[l])
			max_val = max(lsl[l], rsl[l])
			
			if min_val > stall_min:
				new_stall = l
				stall_min = min_val
				stall_max = max_val
			elif min_val == stall_min:
				if max_val > stall_max:
					new_stall = l
					stall_min = min_val
					stall_max = max_val
		
		if k == 1:
			print("Case #" + str(i + 1) + ": " + str(stall_max) + " " + str(stall_min))
			break
		else:
			stalls[new_stall + 1] = True
		
		k -= 1
