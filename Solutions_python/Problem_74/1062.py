class Robot:
	def __init__(self):
		self.pos = 1
		self.reserve = 0
	
	def time(self, pos):
		distance = abs(self.pos - pos)
		distance -= self.reserve
		if distance < 0: distance = 0
		self.reserve = 0
		self.pos = pos
		return distance + 1

def min_time(actions):
	orange, blue = Robot(), Robot()
	tt = 0
	for color, pos in actions:
		if color == 'O':
			t = orange.time(pos)
			blue.reserve += t
			tt += t
		else:
			t = blue.time(pos)
			orange.reserve += t
			tt += t
	return tt

T = int(input().rstrip())
for x in range(1, T+1):
	words = input().rstrip().split(' ')
	N = int(words[0])
	actions = [(words[i], int(words[i+1])) for i in range(1, N*2+1, 2)]
	print('Case #{}: {}'.format(x, min_time(actions)))
