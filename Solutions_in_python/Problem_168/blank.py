for case in range(int(input())):
	R, C = [int(x) for x in input().strip().split()]
	data = [list(input().strip()) for x in range(R)]


	UP    = (-1,  0)
	DOWN  = ( 1,  0)
	LEFT  = ( 0, -1)
	RIGHT = ( 0,  1)

	def free (d, pos):
		i, j = pos[0] + d[0], pos[1] + d[1]

		while i >= 0 and i < R and j >= 0 and j < C:
			if data[i][j] != ".": return False
			i, j = i + d[0], j + d[1]

		return True

	count = 0
	impossible = False

	mapping = {
		"^": UP,
		"v": DOWN,
		"<": LEFT,
		">": RIGHT
	}

	for i in range (R):
		for j in range (C):
			if data[i][j] in mapping and free(mapping[data[i][j]], (i, j)):
				count += 1

				#print ([(free(mapping[dir], (i, j)), dir) for dir in mapping if dir != data[i][j]])
				
				if all ([free(mapping[dir], (i, j)) for dir in mapping if dir != data[i][j]]):
					impossible = True
					break
		
		if impossible: break

	print ("Case #{}: {}".format(case+1, ("IMPOSSIBLE" if impossible else count)))