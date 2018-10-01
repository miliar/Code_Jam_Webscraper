table = {}
table['a'] = 'y'
table['b'] = 'h'
table['c'] = 'e'
table['d'] = 's'
table['e'] = 'o'
table['f'] = 'c'
table['g'] = 'v'
table['h'] = 'x'
table['i'] = 'd'
table['j'] = 'u'
table['k'] = 'i'
table['l'] = 'g'
table['m'] = 'l'
table['n'] = 'b'
table['o'] = 'k'
table['p'] = 'r'
table['q'] = 'z'
table['r'] = 't'
table['s'] = 'n'
table['t'] = 'w'
table['u'] = 'j'
table['v'] = 'p'
table['w'] = 'f'
table['x'] = 'm'
table['y'] = 'a'
table['z'] = 'q'
table[' '] = ' '

input = open('A-small-attempt0.in')
num_of_lines = int(input.readline())
num = 0
output = open('A-small-attempt0.out', 'w')
while num < num_of_lines:
	output.write('Case #' + str(num + 1) + ': ')
	for char in input.readline().strip():
		output.write(table[char])
	output.write('\n')
	num += 1
output.close()
