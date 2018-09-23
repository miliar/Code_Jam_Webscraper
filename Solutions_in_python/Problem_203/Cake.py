def fill(char, grid, pos1, pos2, d_pos):
	for r in range(pos1[0], pos2[0]+1):
		for c in range(pos1[1], pos2[1]+1):
			grid[r][c] = char
			d_pos[char].append((r,c))

def show(grid, writer):
	for row in grid:
		line = ''.join(row)
		writer.write('%s\n' % line)

def main():
	in_file = open('input.in', 'r')
	out_file = open('output.txt', 'w')

	inputs = in_file.readlines()

	T = int(inputs.pop(0).strip())

	for t in range(T):
		#print('t: %d' % (t+1))
		R,C = [int(x) for x in inputs.pop(0).strip().split()]
		grid = []
		for r in range(R):
			line = [x for x in inputs.pop(0).strip()]
			grid.append(line)

		#show(grid)

		d_pos = {}
		for ii in range(len(grid)):
			for jj in range(len(grid[ii])):
				if grid[ii][jj] != '?':
					if grid[ii][jj] not in d_pos.keys():
						d_pos[grid[ii][jj]] = [(ii,jj)]
					else:
						d_pos[grid[ii][jj]].append((ii,jj))

		for k in d_pos.keys():
			min_r, max_r, min_c, max_c = -1, -1, -1, -1
			if len(d_pos[k]) > 1:
				rows = [r for r in d_pos[k]]
				cols = [c for c in d_pos[k]]
				min_r, max_r = min(rows), max(rows)
				min_c, max_c = min(cols), max(cols)
			else:
				min_r = max_r = d_pos[k][0][0]
				min_c = max_c = d_pos[k][0][1]

			#print('char: %s; maxr: %s; minr: %s; maxc: %s; minc: %s' % (k, 	max_r, min_r, max_c, min_c))

			
			while max_c < C-1:
				temp = [grid[x][max_c+1] for x in range(min_r, max_r+1)]
				if temp == ['?']*(max_r-min_r+1):
					max_c += 1
				else:
					break

			while min_c > 0:	
				if [grid[x][min_c-1] for x in range(min_r, max_r+1)] == ['?']*(max_r-min_r+1):
					min_c -= 1
				else:
					break

			while min_r > 0:
				if [grid[min_r-1][x] for x in range(min_c, max_c+1)] == ['?']*(max_c-min_c+1):
					min_r -= 1
				else:
					break

			while max_r < R -1:
				if [grid[max_r+1][x] for x in range(min_c, max_c+1)] == ['?']*(max_c-min_c+1):
					max_r += 1
				else:
					break

			#print('char: %s; maxr: %s; minr: %s; maxc: %s; minc: %s' % (k, 	max_r, min_r, max_c, min_c))

			fill(k, grid, (min_r, min_c), (max_r, max_c), d_pos)
		
		out_file.write('Case #%d:\n' % (t+1))	
		show(grid, out_file)



if __name__ == '__main__':
	main()