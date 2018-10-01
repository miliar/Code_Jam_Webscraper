import math

def collision_time(ps, vs, a, pc, vc):
	v_diff = vs - vc
	p_diff = ps - pc
	return float((math.sqrt((4 * v_diff * v_diff) - (8 * a * p_diff)) - (2 * v_diff))) / float(2 * a)

def solve_sub_case(d, a, car_position_list):
	if len(car_position_list) == 2:
		car_position_pointer = 0
		vs = 0
		ps = 0
		t_ans = 0
		pc = car_position_list[0][1]
		vc = float(car_position_list[car_position_pointer + 1][1] - car_position_list[car_position_pointer][1]) / float(car_position_list[car_position_pointer + 1][0] - car_position_list[car_position_pointer][0])

		t_collision = collision_time(ps, vs, a, pc, vc)
		position = ps + (vs * t_collision) + (0.5 * a * t_collision * t_collision)
		if position < d:
			t_ans = t_collision + ((d - position) / vc)
		else:
			t_ans = collision_time(0, 0, a, d, 0)
	else:
		t_ans = collision_time(0, 0, a, d, 0)
	print t_ans

def solve_case(t):
	line = raw_input().strip().split()
	d = float(line[0])
	n = int(line[1])
	a = int(line[2])
	car_position_list = list()
	n_pointer = 0
	while n_pointer < n:
		car_position_list.append([float(x) for x in raw_input().strip().split()])
		n_pointer += 1
	a_list = [float(x) for x in raw_input().strip().split()]
	print 'Case #%d:' % (t,)
	for a_item in a_list:
		solve_sub_case(d, a_item, car_position_list)

t = int(raw_input().strip())
t_pointer = 1
while t_pointer <= t:
	solve_case(t_pointer)
	t_pointer += 1
