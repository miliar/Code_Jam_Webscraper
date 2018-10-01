fh_read = open('A-large.in')
fh_write = open('output.txt', 'w')

line = fh_read.readline().strip()

num_cases = int(line)

for i in range(num_cases):
	line = fh_read.readline().strip().split()
	num_shyness = [int(c) for c in line[1]]

	num_standing = 0
	friends_needed = 0
	for shyness, count in enumerate(num_shyness):
		if shyness == 0:
			num_standing += count
		elif num_standing < shyness and count > 0:
			friends_needed += shyness - num_standing
			num_standing += shyness - num_standing
			num_standing += count
		else:
			num_standing += count
	fh_write.write("Case #%i: %i\n" % (i + 1, friends_needed))

fh_write.close()
fh_write.close()