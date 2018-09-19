def reverseMap (line):
	i=0
	decode=''
	while i < len(line):
		if line[i] == '\n' or line[i] == '':
			return decode
		if line[i] == ' ':
			decode += ' '
		else:
			decode += mapping[ord(line[i])-ord('a')]
 		i += 1

	
mapping=[]
mapping.append('y')
mapping.append('h')
mapping.append('e')
mapping.append('s')
mapping.append('o')
mapping.append('c')
mapping.append('v')
mapping.append('x')
mapping.append('d')
mapping.append('u')
mapping.append('i')
mapping.append('g')
mapping.append('l')
mapping.append('b')
mapping.append('k')
mapping.append('r')
mapping.append('z')
mapping.append('t')
mapping.append('n')
mapping.append('w')
mapping.append('j')
mapping.append('p')
mapping.append('f')
mapping.append('m')
mapping.append('a')
mapping.append('q')

inputFile = open('A-small.txt', 'r')

n = 0
linenum=0

for line in inputFile:
	if linenum == 0:
		n = int(line)
   	elif linenum > n:
		break
	else:
		if linenum == n:
		    line += '\n'
	        print "Case #{no}: {ret}".format(no=linenum,ret=reverseMap(line))

	linenum += 1