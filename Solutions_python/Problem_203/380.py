import sys
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
ints = []
for i in xrange(1, t + 1):
	#n = raw_input()  # read a list of integers, 2 in this case
	temp = []
	#temp.append(int(n))
	size = [int(s) for s in raw_input().split(" ")]
	temp.append(size)
	rows = []
	for i in xrange(size[0]):
		letters = list(raw_input())
		rows.append(letters)
	temp.append(rows)
	ints.append(temp)
	# print "Case #{}: {} {}".format(i, n + m, n * m)
	# check out .format's specification for more formatting options
# print(ints)





def sol(grid):
	i = 0
	while (rowempty(grid[i])):
		# print(grid[i])
		i+=1
	# print(i)
	for j in xrange(i):
		grid[j] = grid[i]
	j = i
	while(j < len(grid)):
		if (rowempty(grid[j])):
			grid[j] = grid[i]
		else:
			i = j
		j+=1
	for row in grid:
		row = fillrow(row)
	
	return(grid)

	
	
def rowempty(row):
	for ele in row:
		if ele != '?':
			return False
			
	return True
	
def fillrow(row):
	i = 0
	while(row[i] == '?'):
		i+=1
	j = 0
	for j in xrange(i):
		row[j] = row[i]
	j = i

	while(j < len(row)):
	
		if row[j] =='?':
			row[j] = row[i]
		else:
			i=j
		j+=1
	return row
	
#testrow = ['?', '?','I','?', '?','A','?', '?','B','?']

#print(fillrow(testrow))
	

# testgrid = [['?', '?'],['?', 'T'], ['?', '?'],['K', 'E'],['?', '?'],['?', '?'],['?', '?'],['?', '?'],['B', 'A'],['?', '?'],]
# print(sol(testgrid))

#print(list(dfs_paths(graph, 'C', 'F'))) # [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]
			
#sol(ints[3][0],ints[3][1])
	
		
	

	
	
for i in xrange(t):
	print "Case #{}:".format(i+1 )
	res = sol(ints[i][1])
	for row in res:
		print(''.join(row))
	# print "Case #{}: {}".format(i+1, res )
	# print "Case #{}: {} {}".format(i, n + m, n * m)

# for i in xrange(t):
	# print "Case #{}: {} ".format(i+1, sol(ints[i]) )