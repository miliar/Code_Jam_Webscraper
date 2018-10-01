#Google Code Jam 2011, Part A: Bot Trust

def iterateRobot(robot, bPushed, instructions):
	if len(robot.instructions) > 0:
		if robot.position < robot.instructions[0]:
			robot.position += 1
			return False
		elif robot.position > robot.instructions[0]:
			robot.position -= 1
			return False
		else:
			if not bPushed:
				if instructions[0][0] == robot.type:
					instructions.pop(0)
					robot.instructions.pop(0)
					return True
	return False

class robot:
	"""A Robot"""
	def __init__(self, color):
		self.type = color
		self.position = 1
		self.instructions = []

f = open('A-large.in', 'r')
out = open('output.txt', 'w')
cases = int(f.readline())

for i in range(1, cases + 1):
	orange = robot('O')
	blue = robot('B')
	seconds = 0
	instructions = []
	remainingLine = f.readline()
	partitioned = remainingLine.partition(' ')
	count, remainingLine = int(partitioned[0]), partitioned[2]
	for x in range(0, count):
		partitioned = remainingLine.partition(' ')
		bot, remainingLine = partitioned[0], partitioned[2]
		partitioned = remainingLine.partition(' ')
		position, remainingLine = int(partitioned[0]), partitioned[2]
		instructions.append((bot, position))
		if bot == 'O':
			orange.instructions.append(position)
		else:
			blue.instructions.append(position)
	
	while len(instructions) > 0:
		bPushed = False
		bPushed = iterateRobot(orange, bPushed, instructions)
		iterateRobot(blue, bPushed, instructions)
		seconds += 1
	out.write("Case #%d: %d\n" % (i, seconds))
			
out.close()
f.close()