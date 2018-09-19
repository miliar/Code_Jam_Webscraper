def walk(robot):
	if robot['queue'] == []: return False
	nxt_com = robot['queue'][0]
	nxt_pos = nxt_com['button'];
	if robot['position'] == nxt_pos: return True
	if robot['position'] > nxt_pos : robot['position'] = robot['position'] -1
	else : robot['position'] = robot['position'] +1
	return False


def execute_case(blue, orange, commands):
	robots = [blue, orange]
	time = 0
	nxt_com = commands.pop(0)
	executed = False
	while commands != [] or nxt_com != '' :
		time = time +1
		for r in robots:
			if walk(r) and not executed:
				if r['queue'][0] == nxt_com:
					r['queue'].pop(0)
					if commands != []:
						nxt_com = commands.pop(0)
					else: nxt_com = ''
					executed = True
		executed = False

	return time

x = file('A-large.in.in')
n_tests = int(x.readline())
for i in range(0, n_tests):
	blue = { 'position':1, 'queue': []}
	orange = { 'position':1, 'queue': []}


	commands = []
	case = x.readline()
	case_spl = case.split(' ');
	n_com = int(case_spl.pop(0))
	for j in range(0, n_com):
		command = {}
		command['robot'] = case_spl.pop(0)
		command['button'] = int(case_spl.pop(0))
		if 'B'.__eq__(command['robot']) :
			blue['queue'].append(command)
		else:
			orange['queue'].append(command)


		commands.append(command)
	print "Case #%s: %s"%(i+1, execute_case(blue,orange,commands) )


