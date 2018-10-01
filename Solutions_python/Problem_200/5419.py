f = open('B-small-attempt3.in', 'r')
s = f.read()
splitted = s.split('\n')
number_cases = int(splitted[0])
splitted = splitted[1:]
out_s = ''

def is_one_and_zero_only(s):
	if type(s) is int:
		s = str(s)

	for char in s:
		if char != "1" and char != "0":
			return False
	return True

def get_tidy(s):

	if type(s) is int:
		s = str(s)

	if is_one_and_zero_only(s):
		return int((len(s) - 1) * '9')

	prev_char = s[0]
	num = ''
	state = 'idle'
	for char in s[1:]:
		
		if state == 'idle':
			if char < prev_char:
				num = char
				state = 'work'
				
		elif state == 'work':
			num = char

		prev_char = char

	num = int(num) + 1
	in_num = int(s)

	tidy_num = in_num - num

	if is_ascending(tidy_num):
		return tidy_num
	else:
		return get_tidy(tidy_num) 

def is_ascending(s):
	if type(s) is int:
		s = str(s)

	prev_char = s[0]
	for char in s[1:]:
		if char < prev_char:
			return False
		prev_char = char
	return True

counter = 0
for line in splitted:
	if not line:
		continue

	counter += 1

	if len(line) == 1 or is_ascending(line):
		out_s += 'Case #%d: %s\n' % (counter, line)
	else:
		out_s += 'Case #%d: %d\n' % (counter, get_tidy(line))
	
out_s = out_s[0:-1]	

with open('output.txt', 'w') as f:
	f.write(out_s)

