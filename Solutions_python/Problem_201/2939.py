import math

def bathrooms(stalls, people):
	spaces = [stalls]

	while people:
		idx = spaces.index(max(spaces))
		current_space = spaces.pop(idx) - 1

		right_value = int(math.ceil(current_space / 2.0))
		left_value = current_space / 2

		spaces.insert(idx, right_value)
		spaces.insert(idx, left_value)
		people -= 1

	if left_value < right_value:
		left_value, right_value = right_value, left_value
	return left_value, right_value

case_num = -1
with open("input-c") as f:
	for row in f:
		case_num += 1
		if case_num == 0:
			continue
		n, k = [int(x) for x in row.split(' ')]

		answer = bathrooms(n, k)
		print("Case #%s: %s %s" % (case_num, answer[0], answer[1]))


#0000
#0x00