f = open("B-large.in", "r")

output = open("pb_test.out", "w")

T = int(f.readline().rstrip("\n"))

for round in range(1, T+1):
	params = f.readline().rstrip("\n").split(" ")
	C = float(params[0])
	F = float(params[1])
	X = float(params[2])

	# compute
	current_rate = 2.0
	result = X/current_rate

	farm_time = 0.0
	while True:
		farm_time += C/current_rate
		current_rate += F
		new_time = farm_time + X/current_rate
		if new_time > result:
			break
		else:
			result = new_time

	output.write("Case #%d: %.7f\n" % (round, result))

f.close()
output.close()