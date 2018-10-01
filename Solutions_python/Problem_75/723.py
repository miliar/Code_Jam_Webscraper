import sys

fp = open('B-small-attempt0.in', 'r')
n = int(fp.next())

case = 1

for line in fp:
	result = 0
	comb = {}
	clear = {}
	result = []
	
	line = line.split()
	
	for x in range(int(line.pop(0))):
		form = line.pop(0)
		comb[form[0]] = (form[1], form[2])
		comb[form[1]] = (form[0], form[2])
	
	for x in range(int(line.pop(0))):
		form = line.pop(0)
		clear[form[0]] = form[1]
		clear[form[1]] = form[0]
	
	for l in line.pop(1):
		if len(result) == 0:
			result.append(l)
		else:
			if l in comb and comb[l][0] == result[-1]:
				result.pop(-1)
				result.append(comb[l][1])
			elif l in clear and clear[l] in result:
				del result[:]
			else:
				result.append(l) 

	sys.stdout.write('Case #' + str(case) + ': [')
	for i, l in zip(range(len(result)), result):
		if i > 0:
			sys.stdout.write(', ')
		sys.stdout.write(l)
	sys.stdout.write(']\n')
	case += 1

