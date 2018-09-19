import sys
import os

matrix = {'1':{'1':'1', 'i':'i','j':'j','k':'k'},
		  'i':{'1':'i', 'i':'-1', 'j':'k', 'k':'-j'},
		  'j':{'1':'j', 'i':'-k', 'j':'-1', 'k':'i'},
		  'k':{'1':'k', 'i':'j', 'j':'-i', 'k':'-1'},
		  '-1':{'1':'-1', 'i':'-i','j':'-j','k':'-k'},
		  '-i':{'1':'-i', 'i':'1', 'j':'-k', 'k':'j'},
		  '-j':{'1':'-j', 'i':'k', 'j':'1', 'k':'-i'},
		  '-k':{'1':'-k', 'i':'-j', 'j':'i', 'k':'1'}}


def mult(a, b):
	# doesn't support minus in b
	c = matrix[a][b]
	return c

def _reduc(s):
	
	first = '1'
	for i in range(0, len(s)):
		c = s[i]
		first = mult(first, c)
		if first == '1':
			return s[i+1:]

	return s

def reduc(s):

	old_s = ''
	while(old_s != s):
		old_s = s
		s = _reduc(s)
	return s

def solve(l, x, s):

	# try to reduce pattern
#	s = reduc(s)
#	sys.stdout.flush()

	# generate entire string 
	string = ''
	for i in range(x):
		string += s
	size = len(string)

	# find i
	first = '1'
	for i in range(size):

		first = mult(first, string[i])
		if first == 'i':
			break

	string = string[i+1:]
	size = len(string)

	# find j
	second = '1'
	n = 0
	for j in range(size):

		second = mult(second, string[j])
		if second == 'j':
			n = j
			break

	# reduce the expr so that whats left equals k
	string = reduc(string[n + 1:])
	size = len(string)
			
	third = '1'
	for k in range(size):
		third = mult(third, string[k])
		
	if third == 'k':
		return 'YES'

	return 'NO'

def solve_old(l, x, s):

	# generate entire string 
	string = ''
	for i in range(x):
		string += s
	size = len(string)

	first = '1'
	for i in range(size):

		first = mult(first, string[i])
		if first != 'i':
			continue

		second = '1'
		for j in range(i + 1, size):

			second = mult(second, string[j])
			if second != 'j':
				continue

			third = '1'
			for k in range(j+1, size):
				third = mult(third, string[k])
				
			if third == 'k':
				return 'YES'

	return 'NO'



with open(sys.argv[1], 'r') as inputfile, open('ans.out','w') as outputfile:
	 t = int(inputfile.readline())
	 for i in range(t):
	 	(l, x) = (int(j) for j in inputfile.readline().split())
	 	s = inputfile.readline().strip()
	 	print('Solvning case %d (l=%d, x=%d)...' % (i+1, l, x), end='')
	 	sys.stdout.flush()
	 	ans = solve(l, x, s)
	 	outputfile.write('Case #%d: %s\n' % (i +1, ans))
	 	print(ans)

