t = int(raw_input())

class Colour:
	def __init__(self, colour, count):
		self.colour = colour
		self.count = count

answers = []
for test in range(0, t):
	in_str_split = raw_input().split(' ')
	N = int(in_str_split[0])
	R = int(in_str_split[1])
	O = int(in_str_split[2])
	Y = int(in_str_split[3])
	G = int(in_str_split[4])
	B = int(in_str_split[5])
	V = int(in_str_split[6])
	answer = ""

	colours = []
	colours.append(Colour("R", R))
	colours.append(Colour("Y", Y))
	colours.append(Colour("B", B))

	colours.sort(lambda x,y: cmp(x, y), lambda x: x.count, True)

	while colours[0].count > 0:
		if colours[0].count == colours[1].count and colours[0].count == colours[2].count:
			answer += colours[0].colour + colours[1].colour + colours[2].colour
			colours[0].count -= 1
			colours[1].count -= 1
			colours[2].count -= 1
		elif colours[1].count >= colours[2].count:
			answer += colours[0].colour + colours[1].colour
			colours[0].count -= 1
			colours[1].count -= 1
		else:
			answer += colours[0].colour + colours[2].colour
			colours[0].count -= 1
			colours[2].count -= 1

	for colour in colours:
		if colour.count < 0:
			answer = "IMPOSSIBLE"
	answers.append(answer)



for test in range(0, t):
	out_str = "Case #" + str(test+1) + ": " + answers[test]
	print out_str