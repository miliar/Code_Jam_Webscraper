import sys
from numpy import *
from array import *

def ReadVector(file, count):
	return fromfile(file, dtype = int, count = count, sep = ' ')

def ReadMatrix(file, rows, cols):
	return fromfile(file, dtype = int, count = rows * cols, sep = ' ').reshape(rows, cols)

def IsPossible(mtx):
	[rows, cols] = mtx.shape
	done_array = zeros(rows * cols).reshape(rows, cols);

	for cell in xrange(rows * cols):
		# Get the maximum cell.
		max_i = argmax(mtx)
		max_row = max_i / cols
		max_col = max_i % cols
		max_val = mtx[max_row][max_col]
		
		# Verify that there is a row or col that doesn't collision with it.
		for i in xrange(rows):
			if done_array[i][max_col] > max_val:
				for j in xrange(cols):
					if done_array[max_row][j] > max_val:
						return "NO"
				break;

		# Move the current cell to the done matrix.
		done_array[max_row][max_col] = max_val
		mtx[max_row][max_col] = 0

	return "YES"

in_file = open(sys.argv[1], "r")
out_file = open(sys.argv[1] + ".out", "w")

T = int(in_file.readline())

for i in xrange(T):
	[rows, cols] = ReadVector(in_file, 2)
	mtx = ReadMatrix(in_file, rows, cols)
	possible = IsPossible(mtx)
	out_file.write("Case #" + str(i + 1) + ": " + possible + "\n")


in_file.close()
out_file.close()



