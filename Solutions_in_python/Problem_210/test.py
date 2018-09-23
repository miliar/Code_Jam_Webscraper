import fileinput

input = fileinput.input()
cases = int(input.readline())


TOTAL_MINUTES = 1440

def check_activity_between(ac1, ac2, lis2):
	for ac in lis2:
		if (ac[0] > ac1[0] and ac[0] < ac2[0]):
			return True
		if ac1[0] > ac2[0]:
			if ac[0] > ac1[0] or ac[0] < ac2[0]:
				return True
	return False

def sort_time(ac1, ac2):
	if ac1[0] > ac2[0]:
		return 1
	elif ac1[0] == ac2[0]:
		return 0
	else:
		return -1
for case in range(cases):
	number_c, number_j = input.readline().split()
	number_c, number_j = int(number_c), int(number_j)
	c_total = 720
	j_total = 720

	c_ac = []
	j_ac = []
	c_brid = []
	j_brid = []
	for i in range(number_c):
		c_ac.append(input.readline().split())
		c_ac[i][0] = int(c_ac[i][0])
		c_ac[i][1] = int(c_ac[i][1])

	for j in range(number_j):
		j_ac.append(input.readline().split())
		j_ac[j][0] = int(j_ac[j][0])
		j_ac[j][1] = int(j_ac[j][1])


	c_ac.sort(cmp=sort_time)
	j_ac.sort(cmp=sort_time)

	for ac in c_ac:
		j_total -= ac[1] - ac[0]

	for ac in j_ac:
		c_total -= ac[1] - ac[0]
	
	for i in range(len(j_ac)):
		if len(j_ac) == 1:
			break
		if not check_activity_between(j_ac[i], j_ac[(i+1) % len(j_ac)], c_ac):
			value = j_ac[(i+1) % len(j_ac)][0] - j_ac[i][1]
			if value < 0:
				value += TOTAL_MINUTES
			c_brid.append(value)

	j_brid_count = 0
	c_brid_count = 0 



	for i in range(len(c_ac)):
		if len(c_ac) == 1:
			break
		if not check_activity_between(c_ac[i], c_ac[(i+1) % len(c_ac)], j_ac):
			value = c_ac[(i+1) % len(c_ac)][0] - c_ac[i][1]
			if value < 0:
				value += TOTAL_MINUTES
			j_brid.append(value)

	j_brid.sort()
	for brid in j_brid:
		if j_total - brid  >= 0:
			j_total -= brid
			j_brid_count += 1
	c_brid.sort()
	
	for brid in c_brid:
		if c_total - brid  >= 0:
			c_total -= brid
			c_brid_count += 1
	j_ex = 2 * (len(c_ac) - j_brid_count)
	c_ex = 2 * (len(j_ac) - c_brid_count)

	print "Case #%d: %d" % (case + 1, max(j_ex, c_ex))

