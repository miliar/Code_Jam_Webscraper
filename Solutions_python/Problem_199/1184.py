# code jam 2016 qualification A
# N, 2N, 3N... until all digits used otherwise print 'INSOMNIA'
# input file has num of test cases followed by a new N on each line

def first_sad(stack):
	for i in range(len(stack)):
		if stack[i] == '-':
			return i

def flip(stack, pos, size):
	section_to_flip = stack[pos:pos+size]
	flipped_section = ''
	for i in range(size):
		if section_to_flip[i] == '-':
			flipped_section += '+'
		else:
			flipped_section += '-'

	new_stack = stack[:pos] + flipped_section + stack[pos+size:]
	return new_stack

def check_happy(stack):
	return '-' not in stack

t = int(raw_input()) # this is the number of test cases
for i in xrange(1, t+1):
	stack, flipper = raw_input().split(" ")
	flipper = int(flipper)
	num_flips = 0
	while not check_happy(stack) and first_sad(stack) <= len(stack) - flipper:
		stack = flip(stack, first_sad(stack), flipper)
		num_flips += 1

	if check_happy(stack):
		print  "Case #{}: {}".format(i, num_flips)
	else:
		print  "Case #{}: IMPOSSIBLE".format(i)

