"""
Google Code Jam Qualifier #2
"""

def tidy_numbers(num):
	str_num = [i for i in str(num)]
	if len(str_num) == 1:
		return ''.join(str_num)
	else:
		change = 1
		while change != 0:
			change = 0
			for prev in range(len(str_num) - 1):
				a_next = prev + 1
				if int(str_num[prev]) <= int(str_num[a_next]):
					pass
				elif str_num[prev] == '1' and  str_num[a_next] == '0':
					str_num[prev] = '0'
					str_num[a_next] = '9'
					change += 1
				else:
					if change > 0:
						str_num[a_next] = '9'
						change += 1
					else:
						prev_num = int(str_num[prev])
						str_num[prev] = str(prev_num - 1)
						str_num[a_next] = '9'
						change += 1
	while str_num[0] == '0':
		str_num.pop(0)
	return ''.join(str_num)

t= int(raw_input().strip())
for i in range(t):
	num = int(raw_input().strip())
	answer = tidy_numbers(num)
	print "Case #" + str(i+1) + ": " + answer
