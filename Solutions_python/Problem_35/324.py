#!/usr/bin/python

def readInput():
	file = open("B-large.in")

	mapCount = int(file.readline().rstrip())
	maps = []

	for i in range(0, mapCount):
		height, width = [int(i) for i in file.readline().rstrip().split(" ")]

		maps.append((height, width, [[int(i) for i in file.readline().rstrip().split(" ")] for j in range(0, height)]))

	return maps

def traceFlows(mapData):
	height, width, map = mapData
	
	flowMap = []

	for y in range(0, height):
		row = []

		for x in range(0, width):
			# north, west, east, south
			directions = [True, True, True, True]
			altitudes = []

			# north
			if y == 0:
				altitudes.append(None)
			else:
				altitudes.append(map[y-1][x])

			# west
			if x == 0:
				altitudes.append(None)
			else:
				altitudes.append(map[y][x-1])

			# east
			if x == width - 1:
				altitudes.append(None)
			else:
				altitudes.append(map[y][x+1])

			# south
			if y == height - 1:
				altitudes.append(None)
			else:
				altitudes.append(map[y+1][x])

			for i in range(0,4):
				for j in range(0,4):
					if i == j:
						# don't compare with self
						continue

					if altitudes[i] is None:
						# ignore non-existent cells
						directions[i] = False
						continue

					if altitudes[i] >= map[y][x]:
						# no difference
						directions[i] = False
						continue

					if altitudes[j] is None:
						# don't compare with non-existent cells
						continue

					if altitudes[i] > altitudes[j]:
						# cell is higher than other cell
						directions[i] = False
						continue

			found = False

			for i in range(0,4):
				if directions[i]:
					row.append(i)
					found = True
					break

			if not found:
				row.append(-1)

		flowMap.append(row)

	return (height, width, flowMap)

directions = [
	(0,-1), # north - 0
	(-1,0), # west - 1
	(1,0), # east - 2
	(0,1), # south - 3
]

def identifyBasins(mapData):
	height, width, flowMap = mapData

	basinMap = [[None for i in range(0,width)] for j in range(0,height)]

	basinNum = 1

	for y in range(0,height):
		for x in range(0,width):
			stack = [(x,y)]

			while stack:
				x,y = stack.pop()

				if basinMap[y][x]:
					# the cell is already identified
					continue

				direction = flowMap[y][x]
				if direction == -1:
					# identified a sink
					basinMap[y][x] = basinNum
					basinNum += 1
					continue

				stack.append((x,y))

				x2 = x + directions[direction][0]
				y2 = y + directions[direction][1]

				if basinMap[y2][x2]:
					# found a stream
					basinMap[y][x] = basinMap[y2][x2]
					continue

				stack.append((x2,y2))
	
	return basinMap

input = readInput()
flowMaps = [traceFlows(map) for map in input]
basinMaps = [identifyBasins(flowMap) for flowMap in flowMaps]

case = 1
base = ord('a') - 1

for map in basinMaps:
	print "Case #%s:" % case
	case += 1
	for line in map:
		print ' '.join([chr(base + i) for i in line])
