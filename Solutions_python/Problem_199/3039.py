def parse_line(str):
    t = str.split()
    k_size = int(t[1])
    pancakes_by_up = [c == '+' for c in t[0]]
    return pancakes_by_up, k_size


def solve(str):
	pancakes_by_up, k_size = parse_line(str)
	
	num_of_pancakes = len(pancakes_by_up)
	num_of_flips = 0
	flip_state = False
	should_change_flip_state = [False] * num_of_pancakes
	
	for pancake_ind in range(0,num_of_pancakes):
		real_pancake_state = pancakes_by_up[pancake_ind] ^ flip_state
		flip_state = flip_state ^ should_change_flip_state[pancake_ind]
		if( not real_pancake_state):
			if( pancake_ind < num_of_pancakes - k_size + 1):
				num_of_flips += 1
				flip_state = not flip_state
				should_change_flip_state[pancake_ind + k_size - 1] = True
			else:
				return "IMPOSSIBLE"

	return str(num_of_flips)
		
	