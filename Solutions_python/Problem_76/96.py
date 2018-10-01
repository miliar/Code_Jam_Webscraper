from collections import defaultdict
input = open("CandySplitting.in")
output = open("CandySplitting.out", "w")
T = int(input.readline())
for t in range(T):
	N = int(input.readline())
	seq = [int(n) for n in input.readline().split(" ")]
	r = 0
	sum = 0
	for i in seq:
		r ^= i
		sum += i
	max = 0
	for i in seq:
		if i == r ^ i:
			if sum - i > max:
				max = sum - i
			elif i > max:
				max = i
	if max == 0:
		max = "NO"
	print("Case #{case}: {result}".format(case = t + 1, result = max), file = output)
