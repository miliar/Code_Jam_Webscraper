fp_in = open('A-large.in', 'r')
fp_out = open('qual-a-largeout.txt', 'w')

def process_case(case):
	args = case.split(' ')
	max_shyness = args[0]
	levels = args[1].strip()
	num_standing = int(levels[0])
	friends_req = 0
	shyness_level = 0

	for num_at_shyness_level in levels[1:]:
		shyness_level = shyness_level + 1
		num_at_shyness_level = int(num_at_shyness_level)
		num_new_friends = 0
		if shyness_level > num_standing:
			num_new_friends = num_new_friends + (shyness_level - num_standing)
		num_standing = num_standing + num_at_shyness_level + num_new_friends
		friends_req = friends_req + num_new_friends
	return friends_req

case_num = 1
cases = fp_in.readlines()
for case in cases[1:]:
	output_str = "Case #{0}: {1}\n".format(case_num, process_case(case))
	# print(output_str)
	fp_out.write(output_str)
	case_num = case_num + 1
fp_in.close()
fp_out.close()