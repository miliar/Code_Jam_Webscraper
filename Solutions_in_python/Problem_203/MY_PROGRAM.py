t = int(input())
for i in range(1, t + 1):
	nums = input().split(" ")
	m = int(nums[0])
	n = int(nums[1])
	result = [[0 for _ in range(n)] for _ in range(m)]
	index = []
	done = []
	target = ["?"] * n
	for j in range(m):
		letters = list(input())
		if letters == target:
			index.insert(0,j)
		else:
			temp = [[l,letters[l]] for l in range(n) if letters[l] != "?"]
			length = len(temp)
			for k in range(length):
				if k == 0:
					result[j][:temp[k][0]+1] = temp[k][1] * (temp[k][0]+1)
				else:
					result[j][temp[k-1][0]+1:temp[k][0]+1] = temp[k][1] * (temp[k][0]-temp[k-1][0])
			result[j][temp[length-1][0]+1:] = temp[length-1][1] * (n-temp[length-1][0]-1)
			done.insert(0,j)
	while index and done:
		a = done.pop()
		while index and index[-1] < a:
			result[index.pop()] = result[a][:]
	for j in index:
		result[j] = result[a][:]
	print("Case #{}:".format(i))
	for j in range(m):
		print("".join(result[j]))