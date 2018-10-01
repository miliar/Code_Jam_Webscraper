import math

file_strings = []
with open("A-large.in") as data_file:
	for line in data_file:
		file_strings.append(line.strip())


T = file_strings[0] # number of testcases
file_strings.pop(0)
T = int(T)

for i in range (1, T + 1):
	vals = file_strings.pop(0).split()
	D, N = int(vals[0]), int(vals[1]	)
	# positions and speeds of other horses on the road
	positions = []
	speeds = []

	for j in range(N):
		nums = file_strings.pop(0).split()
		pos, speed = int(nums[0]), int(nums[1])
		positions.append(pos)
		speeds.append(speed)

	maxTime = 0
	mySpeed = 0
	for k in range(N):
		time = float(D - positions[k])/float(speeds[k])
		if time > maxTime:
			maxTime = time
			mySpeed = float(D)/float(maxTime)
	print("Case #{}: {}".format(i, mySpeed))