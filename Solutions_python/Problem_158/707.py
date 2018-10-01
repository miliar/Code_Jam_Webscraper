f = open('input.txt', 'r')
def function(pancakes):
	time = 0
	while pancakes[-1] > 0:
		if pancakes[-1] > 3:
			half = pancakes[-1]//2
			pancakes[-1] -= half
			pancakes.append(half)
			pancakes = sorted(pancakes)
		else:
			pancakes[:] = [x - 1 for x in pancakes]
		time += 1
	return time
T = int(f.readline())
for i in xrange(T):

	noOfDiners = int(f.readline())
	pancakes = f.readline().split(' ')

	for j in range(noOfDiners):
		pancakes[j] = int(pancakes[j])

	pancakes = sorted(pancakes)

	print("Case #" + str(i+1) + ": " + str(function(pancakes)))
	# 3 4 4 4 4 4 3 4