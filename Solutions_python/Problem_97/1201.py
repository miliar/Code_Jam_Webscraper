import sys

def isDistinctPair(x, y):
	x = str(x)
	y = str(y)
	for i in range(1, len(x)):
		tail = x[i:]
		if (y.startswith(tail)):
			if (y.endswith(x[0:i])):
				return True
	return False


f = open(sys.argv[1], "r")

f.readline()
line = f.readline()
tc = 1
while (line):
	count = 0
	nums = line.split()
	A = int(nums[0])
	B = int(nums[1])
	
	for x in range(A, B):
		for y in range(x+1, B+1):
			if (isDistinctPair(x, y)):
				count += 1
	
	print("Case #" + str(tc) + ": " + str(count))		
	tc += 1
	line = f.readline()
	
f.close()
