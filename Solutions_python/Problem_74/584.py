def test_cases():
	from sys import stdin
	
	stdin.readline()
	for line in stdin:
		yield line.strip().split(' ')[1:]

for (case_number, case_data) in enumerate(test_cases()):
	# The state variables
	t = 0
	robot_locs = {'O': 1, 'B': 1}
	robot_presses = {'O':[], 'B':[]}
	all_presses = []
	
	# Read case data into state
	for (robot, loc) in zip(case_data[::2], case_data[1::2]):
		all_presses.append(robot)
		robot_presses[robot].append(int(loc))

	while len(all_presses) > 0:
		t += 1
		pressing = False

		for robot in (robot for robot in robot_presses if len(robot_presses[robot]) > 0):
			# If the robot is not in the spot it needs to be in for the next press, move it
			if not robot_presses[robot][0] == robot_locs[robot]:
				loc_diff = robot_presses[robot][0] - robot_locs[robot]
				robot_locs[robot] += cmp(loc_diff, 0)
				
			# If the robot is positioned correctly, the other isn't pressing, and it's its turn to press
			elif not pressing and all_presses[0] == robot:
				all_presses.pop(0)
				robot_presses[robot].pop(0)
				pressing = True
			
			else:
				pass # staying
			
	print "Case #%d: %d" % (case_number+1, t)