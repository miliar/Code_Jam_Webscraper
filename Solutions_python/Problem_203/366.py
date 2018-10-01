import sys
import os

def fill_row(starting_row, starting_col, grid_row, R, C):
	character = grid_row[starting_row][starting_col]
	i_start = starting_row
	j_start = starting_col - 1
	while (j_start >= 0 and grid_row[i_start][j_start] == "?"):
		grid_row[i_start][j_start] = character
		j_start -= 1

	j_start = starting_col + 1
	while (j_start < C and grid_row[i_start][j_start] == "?"):
		grid_row[i_start][j_start] = character
		j_start += 1

def find_next_row(grid_row, R, C, i):
	# print("find_next_row, with, i = ", i)
	i_start = i - 1
	while (i_start >= 0 and grid_row[i_start][0]=="?"):
		i_start -= 1
	if i_start != -1:
		return i_start
	else:
		i_start = i + 1
		while (i_start < R and grid_row[i_start][0]=="?"):
			i_start += 1
		return i_start


T = int(input())
for t in range(T):
	R, C = list(map(int, input().split()))
	grid_row = []
	grid_column = ["" for j in range(C)]
	for i in range(R):
		row = list(input())
		grid_row.append(row)

	# print(grid_row)
	# print(grid_column)

	for i in range(R):
		for j in range(C):
			if grid_row[i][j]!="?":
				# Determine the largest square you can do
				# Otherwise, just pick the most longest one
				fill_row(i, j, grid_row, R, C)

	# print(grid_row)

	for i in range(R):
		s = ''.join(grid_row[i])
		if (grid_row[i][0]=="?"):
			# print("row with ? find with i = ", i)
			i_cop = find_next_row(grid_row, R, C ,i)
			# print("i_cop : ", i_cop)
			st = ''.join(grid_row[i_cop])
			grid_row[i] = list(st)

	# print(grid_row)
	print("Case #" + str(t+1) + ":")
	for i in range(R):
		s = ''.join(grid_row[i])
		print(s)



