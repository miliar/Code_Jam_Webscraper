
def flip(pancake, r):
	sub_pancake = pancake[r[0]:r[1]]
	left_context = pancake[0:r[0]]
	right_context = pancake[r[1]:]
	return left_context + ''.join([ '+' if p == '-' else '-' for p in sub_pancake]) + right_context

def get_distance(pancake, k):
	edge = 0
	count = 0
	for i in range(len(pancake)):
		if pancake[edge] != '+':
			if (edge+k) > len(pancake):
				break
			pancake = flip(pancake, (edge, edge + k))
			count += 1
			edge += 1
		else:
			edge += 1

	if '-' in pancake:
		return "IMPOSSIBLE"
	else:
		return count


input_file_name = 'A-large.in'
output_file_name = 'A-large.out'

output_line_template = "Case #%d: %s"
outputs = []

with open(input_file_name, 'r') as input_file:
	num_tests = int(input_file.readline().strip())
	for test_id in range(1, num_tests+1):
		line = input_file.readline().strip()
		pancake, k = line.split()
		print (pancake, k)
		min_dist = get_distance(pancake, int(k))
		print (min_dist)
		outputs.append(output_line_template % (test_id, str(min_dist)))

with open(output_file_name, 'w') as output_file:
	output_file.write('\n'.join(outputs))



