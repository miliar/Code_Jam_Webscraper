import sys

in_file = open(sys.argv[1])
out_file = open("out.txt", 'w')


RED = "Red"
BLUE = "Blue"
BOTH = "Both"
NEITHER = "Neither"

NESW = "NESW"
NWSE = "NWSE"
HORIZONTAL = "HORIZONTAL"

COLOURS = {"R": (RED, BLUE), "B": (BLUE, RED)}

T = int(in_file.readline().strip())
for t in xrange(T):
	N, K = (int(x) for x in in_file.readline().strip().split())
	cols = []
	line_check = {}
	for direction in NESW, NWSE, HORIZONTAL:
		line_check[direction] = {}
		line_check[direction][RED] = [0 for x in range(N*2)]
		line_check[direction][BLUE] = [0 for x in range(N*2)]
	red_line = "R" * K
	blue_line = "B" * K
	result = NEITHER
	for n in xrange(N):
		col = in_file.readline().strip().replace(".", "")
		if result != BOTH:
			if red_line in col:
				if result == BLUE:
					result = BOTH
				else:
					result = RED
			if blue_line in col:
				if result == RED:
					result = BOTH
				else:
					result = BLUE	
			col = list(reversed(col))
			if result != BOTH:
				for i in xrange(len(col)):
					colour, anti_colour = COLOURS[col[i]]
					for direction, pos in ((HORIZONTAL, i), (NESW, i+n), (NWSE, i+N-n)):
						line_check[direction][colour][pos] += 1
						line_check[direction][anti_colour][pos] = 0
						if line_check[direction][colour][pos] == K:
							if result == anti_colour:
								result = BOTH
								break
							else:
								result = colour
					if result == BOTH:
						break
	output = "Case #%d: %s\n" % (t+1, result)
	print output,
	out_file.write(output)

out_file.close()