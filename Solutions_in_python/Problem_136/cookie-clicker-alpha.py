def calc_time(cost_farm, ecps, goal, farm):
	time = 0
	cps = 2
	for i in range(farm):
		time += cost_farm/cps
		cps += ecps
	time += goal/cps
	return time

def best_strategy(cost_farm, ecps, goal):
	farm = 0
	while True:
		current = calc_time(cost_farm, ecps, goal, farm)
		better = calc_time(cost_farm, ecps, goal, farm+1)
		farm += 1
		if current < better:
			break
	return current

input_file = open("B-small-attempt0.in")
input_data = input_file.read().split("\n")

testcase = input_data.pop(0)
input_data.pop()
case = 1
for input_row in input_data:
	input_row = input_row.split(" ")
	goal = float(input_row.pop())
	ecps = float(input_row.pop())
	cost_farm = float(input_row.pop())
	spent_time = best_strategy(cost_farm, ecps, goal)
	print("Case #{:d}:".format(case), format(spent_time, ".7f"))
	case += 1

input_file.close()

