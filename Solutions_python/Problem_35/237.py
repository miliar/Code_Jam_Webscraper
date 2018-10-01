#!/usr/bin/env python

########################################
def min_neigh(h, w, map):
	neighbours = []
	dirs = [[-1, 0], [0, -1], [0, 1], [1,0]]
	max = 100001
	#north
	if h > 0:
		neighbours.append(int(map[h-1][w]))
	else:
		neighbours.append(max)
	#west
	if w > 0:
		neighbours.append(int(map[h][w-1]))
	else:
		neighbours.append(max)
	#east
	if w < W-1:
		neighbours.append(int(map[h][w+1]))
	else:
		neighbours.append(max)
	#south
	if h < H-1:
		neighbours.append(int(map[h+1][w]))	
	else:
		neighbours.append(max)
	
	
	lo = min(neighbours)
	
	for i in range(4):
		if neighbours[i] is lo:
			return neighbours[i], dirs[i]

########################################
def dfs(h, w, map, result, label):
	if result[h][w] is not '':
		return result, result[h][w]
	else:
		result[h][w] = label
		minim, dir = min_neigh(h, w, map)
		if int(map[h][w]) > minim:
			return dfs(h+dir[0], w+dir[1], map, result, label)
		else:
			return result, label

########################################
file = open("B-large.in", "r")
input = iter(file.readlines())
output = open("output.txt", "w");
totalCases = int(input.next())
labels = 'abcdefghijklmnopqrstuvwxyz'

for case in range(totalCases):
	
	
	output.write('Case #%d:\n' % (case+1))
	map = []
	result = []
	H, W = input.next().split(" ")
	H = int(H)
	W = int(W)
	h = 0
	w = 0
	found = True
	nowLabel = 0
	
	for i in range(H):
		map += [input.next()[:-1].split(" ")]
		result += [[''] * W]
	
	while found:
		found = False
		#first unlabeled cell 
		for i in range(H):
			for j in range(W):
				if result[i][j] is '':
					h = i
					w = j
					found = True
					break
					
			if found:
				break
				
		result, label = dfs(h, w, map, result, '.')
		if label is '.':
			label = labels[nowLabel]
			nowLabel +=1
		
		for i in range(H):
			for j in range(W):
				if result[i][j] is '.':
					result[i][j] = label

	for line in result:
		for cell in line:
			output.write(cell +' ')		
		output.write('\n')	

output.close()
file.close()


	
