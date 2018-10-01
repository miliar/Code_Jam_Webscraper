import sys

t = int(sys.stdin.readline())

for count in range(1, t+1):
	num = int(sys.stdin.readline())
	values = sys.stdin.readline()
	tokens = values.split()
	
	values = map(int, tokens)

	x_sum = 0
	sum = 0
	for value in values:
		x_sum = x_sum ^ value
		sum += value
	
	if x_sum != 0:
		print "Case #" + str(count) + ": NO"
	else:
		print "Case #" + str(count) + ": " + str((sum-min(values)))
print 
