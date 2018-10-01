from sys import argv
from os.path import expanduser


# Import the file as a list of lines:
problem = argv[1]
path = expanduser('~/Downloads/')
file_in = path + problem + '.in'
file_out = path + problem + '.out.txt'


def A(pancakes,n):
	flips = 0
	for i in xrange(len(pancakes)-n+1):
		print pancakes, i, n
		if pancakes[i] == '+':
			continue
		for d in xrange(n):
			if pancakes[i+d] == '-':
				pancakes[i+d] = '+'
			else:
				pancakes[i+d] = '-'
		flips += 1
	if '-' in pancakes:
		return 'IMPOSSIBLE'
	else:
		return str(flips)

'''
nums = ['---+-++- 3','+++++ 4','-+-+- 4']
for num in nums:
	ls = num.split()
	print A(list(ls[0]),int(ls[1]))
'''


with open(file_in,'rb') as fin, open(file_out,'wb') as fout:
	
	lines = fin.read().splitlines()
	case = 1

	for l in lines[1:]:
		ls = l.split()
		n = list(ls[0])
		k = int(ls[1])
		
		answer = A(n,k)

		output = 'Case #%d: %s\n' % (case,answer)
		fout.write(output)
		case += 1
