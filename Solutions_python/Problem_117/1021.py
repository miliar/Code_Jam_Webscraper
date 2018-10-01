import sys


# Read data file into a list
lines = []
with open(sys.argv[1], "r", encoding="utf-8") as data_file:
	for line in data_file:
		lines.append(line.rstrip('\n'))


# Get total number of test cases
test_cases = int(lines[0])
del lines[0]

# Process each test case
for i in range(test_cases):
	
	# Gather data
	rows = int(lines[0].split(" ")[0])
	columns = int(lines[0].split(" ")[1])
	del lines[0]
	
	grass = []
	marked = []
	for j in range(rows):
		grass.append([int(k) for k in lines[0].split(" ")])
		marked.append([0,] * columns)
		del lines[0]
		
	
	# Iterate through each grass square and analyze
	# horizontal and vertical swaths at that square
	for j in range(rows):
		for k in range(columns):
			tmpCol = []
			for l in range(rows):
				tmpCol.append(grass[l][k])
			
			if max(grass[j]) <= grass[j][k]:
				for l in range(columns):
					if grass[j][l] == grass[j][k]:
						marked[j][l] = 1
			
			if max(tmpCol) <= grass[j][k]:
				for l in range(rows):
					if grass[l][k] == grass[j][k]:
						marked[l][k] = 1
		
	# If any squares are unmarked, then fail
	flag = False
	for j in range(rows):
		if marked[j].count(0) > 0:
			flag = True
			
	if flag == True:
		print("Case #" + str(i + 1) + ": NO")
	else:
		print("Case #" + str(i + 1) + ": YES")	

