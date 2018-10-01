f = open('input.txt', 'r')
def function(pancakes, t):

	# a = 6
	# if t == a:
	# 	print(pancakes)
	# # print('pancakes',pancakes)
	biggest = pancakes[-1]
	indexOfBiggest = pancakes.index(biggest)
	numberOfBiggestPancakes = len(pancakes)- indexOfBiggest	
	time = 0
	# print(numberOfBiggestPancakes)
	while pancakes[-1] > 0:
		while len(pancakes) != 0 and pancakes[0] == 0:
			pancakes = pancakes[1:]
		length = len(pancakes)
		if  length == 0:
			break

		biggest = pancakes[-1]
		indexOfBiggest = pancakes.index(biggest)
		numberOfBiggestPancakes = length - indexOfBiggest

		if numberOfBiggestPancakes + (biggest+1)//2 < biggest:
			# pancakes[:] = [x - 1 for x in pancakes]
			# 
		# elif (length == 1 and pancakes[0] > 2) or (pancakes[-1] > 3 and (pancakes[-1] - pancakes[0] > 1 or pancakes[-1] > 4)):
			if biggest == 9:
				pancakes1 = pancakes[:]
				pancakes2 = pancakes[:]

				pancakes1[-1] = 6
				pancakes1.append(3)

				pancakes1 = sorted(pancakes1)
				
				pancakes2[-1] = 5
				pancakes2.append(4)
				pancakes2 = sorted(pancakes2)

				time1 = function(pancakes1, t)
				time2 = function(pancakes2, t)
				# print(time, time1, time2)
				return min(time + 1 + time1, time + 1 + time2)
			else:	
				half = pancakes[-1]//2
				pancakes[-1] -= half
				pancakes.append(half)
			pancakes = sorted(pancakes)
		else:
			pancakes[:] = [x - 1 for x in pancakes]

		# if t == a:
		# 	print(pancakes)
		time += 1

	return time


T = int(f.readline())
for i in xrange(T):

	noOfDiners = int(f.readline())
	pancakes = f.readline().split(' ')

	for j in range(noOfDiners):
		pancakes[j] = int(pancakes[j])

	pancakes = sorted(pancakes)
	# if max(pancakes) == 9:
	# 	print(i+1, pancakes)
	print("Case #" + str(i+1) + ": " + str(function(pancakes, i+1)))
	# 3 4 4 4 4 4 3 4