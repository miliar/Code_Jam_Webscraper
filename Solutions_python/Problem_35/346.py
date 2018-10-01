from __future__ import with_statement
import sys
import string

def readInt(f):
	return int(f.readline().strip())

def follow(map, basins, h, w, index, label):

	#so we need to follow the flow from index
	if basins[index] != "0":
		#we've already been labelled
		return basins[index]

	altitude = map[index]

	#neighbours in order
	neighbours = [index - w]

	if (index % w) != 0: #western point on map
		neighbours.append(index - 1)

	if (index + 1) % w != 0: #eastern point on map
		neighbours.append(index + 1)

	neighbours.append(index + w)

	lowest = altitude #limit is actuall 10k
	lowestNeighbour = -1 

	for neighbour in neighbours:
		if neighbour >= 0 and neighbour < len(map):
			if map[neighbour] < lowest:
				lowest = map[neighbour]
				lowestNeighbour = neighbour

	if lowestNeighbour == -1:
		#sink
		basins[index] = label
		return label
	else:

		newLabel = follow(map, basins, h, w, lowestNeighbour, label)
		basins[index] = newLabel
		return newLabel

def solve(map, h, w):
	basins = ["0" for foo in xrange(w * h)]

	labelIndex = 0

	while "0" in basins:
		i = basins.index("0")

		label = string.letters[labelIndex]

		usedLabel = follow(map, basins, h, w, i, label)

		if label == usedLabel:
			labelIndex += 1

	#convert it back to the format we need
	answer = "\n"
	for i in xrange(len(basins)):
		if (i + 1) % w == 0:
			answer += basins[i]
			answer += "\n"
		else:
			answer += basins[i] + " "

	return answer.rstrip()

if __name__ == "__main__":
	file = sys.argv[1]
	output = "%s.out" % (file, )

	answers = []

	with open(file) as f:
		numMaps = readInt(f)
		for i in xrange(numMaps):
			h, w = [int(foo) for foo in 
					f.readline().strip().split(" ")]

			map = []
			for q in xrange(h):
				map.extend([int(foo) for foo in f.readline().strip().split()])

			answers.append(solve(map, h, w))

	i = 0
	with open(output, 'w') as f:
		for answer in answers:
			i += 1
			f.write("Case #%d: %s\n" % (i, answer))

