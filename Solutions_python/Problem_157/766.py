def read(path):
	file_in = open(path, 'r')

	# No file out; Use "python A.py > A_out_small.txt"

	case = 0
	start = 0
	# l = []
	length = -1
	times = -1
	for line in file_in:
		# print line
		if case == 0:
			case += 1
		else:
			temp = line.split()
			if len(temp) == 2:
				length = int(temp[0])
				times = int(temp[1])
				# print "Length and time", length, times
			else:
				sub_str = str(temp[0])
				# print "Sub_str = ", sub_str

				# Solve
				result = solve(sub_str, length, times)

				# Print
				print "Case #" + str(case) + ": " + result

				# Update case, length and times
				case += 1
				length = -1
				times = -1

def mult(a, b):
	if a == '1' and b == '1':
		return '1'
	if a == b and a != '1':
		return '-1'
	if (a == '1' or a == 'i') and (b == 'i' or b=='1'):
		return 'i'
	if (a == '1' or a=='j') and (b == 'j' or b=='1'):
		return 'j'
	if (a == '1' or a=='k') and (b == 'k' or b=='1'):
		return 'k'	
	if (a == 'i') and (b=='j'):
		return 'k'
	if (a == 'j') and (b=='i'):
		return '-k'
	if (a == 'j') and (b=='k'):
		return 'i'
	if (a == 'k') and (b=='j'):
		return '-i'
	if (a == 'i') and (b=='k'):
		return '-j'
	if (a == 'k') and (b=='i'):
		return 'j'

def solve(s, length, times):
	if length == 1:
		return 'NO'
	if length*times == 3:
		if s != "ijk":
			return 'NO'
		else:
			return 'YES'
	else:
		s_new = s*times
		# print s_new
		glob_count = 0
		# print(s_new)
		# Try each char * char
		# Get the max length of a substring
		sub = []
		# 0 == 'i', 1 == 'j', 2 == 'k'
		now = {0 : 'i', 1 : 'j', 2 : 'k'}
		count = 0
		curr = ""

		for i in range(len(s_new)):
			# print('i is: ' + str(i))
			# print(curr)
			# print(glob_count)
			if len(curr) == 0:
				curr += s_new[i]
			else:
				# Get curr last element
				if len(curr) == 2:
					# It's a negative number
					temp = mult(curr[1], s_new[i])
					if len(temp) == 2:
						curr = temp[1]
					else:
						curr = "-" + temp
				else:
					curr = mult(curr, s_new[i])
			# Check curr
			if curr == now[count]:
				if count == 2 and i < len(s_new) - 1:
					# Keep going
					pass
				else:
					glob_count += 1
					count += 1
					curr = ""
			else:
				pass

		# Check glob_count
		if glob_count == 3:
			return 'YES'
		else:
			return 'NO'

# read("B_tests_in.txt")
read("C-small-attempt0.in")