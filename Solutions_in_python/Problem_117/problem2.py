import numpy as np

INPUT_FILE = "./input2.txt"

RESULT = ""

MIN_POSSIBLE_HEIGHT = 1
MAX_POSSIBLE_HEIGHT = 100

def find_max_height(lawn):
	max_height = MIN_POSSIBLE_HEIGHT

	for line in lawn:
		for col in line:
			if col > max_height:
				max_height = col

	return max_height

def find_next_max_height(lawn, min):
	max_height = MIN_POSSIBLE_HEIGHT

	for line in lawn:
		for col in line:
			if col < min and col > max_height:
				max_height = col

	return max_height

def can_cut(itens, height):
	for item in itens:
		if item > height:
			return False

	return True


def get_all_heights(lawn):
	heights = []

	for line in lawn:
		for col in line:
			heights.append(col)

	return sorted(set(heights), reverse = True)

def find_min_height(lawn):
	min_height = MAX_POSSIBLE_HEIGHT

	for line in lawn:
		for col in line:
			if col < min_height:
				min_height = col

	return min_height

def column(matrix, i):
    return [row[i] for row in matrix]

if __name__ == "__main__":

	# input file
	lines = [line.strip() for line in open(INPUT_FILE) if line.strip()]

	print "Total entries: ", lines[0]
	print "Total lines: ", len(lines)

	curPos = 1

	# read boards
	for boardNum in xrange(int(lines[0])):
		RESULT += "Case #" + str(boardNum + 1) + ": "

		dimensions = lines[curPos].split()
		print "Grass [w: " + dimensions[1] + ", h: " + dimensions[0] + "]"
		curPos += 1

		width = int(dimensions[1])
		height = int(dimensions[0])
		lawn_shape = []
		for linePos in xrange(curPos, curPos + height):
			ln = list(lines[linePos])
			ln = [int(x) for x in ln if x.strip()] # remove spaces

			lawn_shape.append(ln)
			curPos += 1

		min_height = find_min_height(lawn_shape)
		max_height = find_max_height(lawn_shape)

		lawn = [[MAX_POSSIBLE_HEIGHT for x in xrange(width)] for x in xrange(height)] 
		
		# put our lawn on the higher height
		for y in xrange(height):
			for x in xrange(width):
				lawn[y][x] = max_height

		# first column
		lawn_columns = [column(lawn_shape, 0), column(lawn_shape, -1)]
		lawn_lines = [lawn_shape[0], lawn_shape[-1]]

		edges = [
			lawn_lines[0], # top
			lawn_columns[1], # right
			lawn_lines[1], # bottom
			lawn_columns[0] # left
		]

		# Calculations
		all_heights = get_all_heights(lawn_shape)
		for ch in all_heights:
			for e in xrange(len(edges)):
				is_line = e % 2 != 0

				for i in xrange(len(edges[e])):
					edge_data = lawn_shape[i] if is_line else column(lawn_shape, i)
					layout_height = edges[e][i]
					
					we_can_cut = can_cut(edge_data, ch)
					if layout_height <= ch and we_can_cut:
						if is_line:
							for x in xrange(len(lawn[i])):	
								lawn[i][x] = ch
						else:
							for y in xrange(len(lawn)):
								for x in xrange(len(lawn[y])):
									if x == i:
										lawn[y][x] = ch


		#print "Original Lawn"
		#print lawn_shape
		#print "Final Lawn"
		#print lawn

		if lawn == lawn_shape:
			RESULT += "YES"
		else:
			RESULT += "NO"


		RESULT += "\n"

	print "==================================="
	print RESULT
	print "==================================="

	output = open('./output2.txt','w')
	output.write(RESULT)
	output.close()