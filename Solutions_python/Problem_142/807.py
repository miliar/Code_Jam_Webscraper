import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

with open('input.in','r') as f:
	lines = f.readlines()
f.close()
f = open('output.out','w')

T = int(lines[0])

case = 0
l = 1
while case < T:
	case += 1
	strings = []
	for s in range(1,int(lines[l])+1):
		my_s = []
		cp = ''
		for char in lines[l+s].strip():
			if char != cp:
				my_s.append([char,1])
				cp = char
			else:
				my_s[-1][1] += 1
		strings.append(my_s)

	if len(set([''.join([c[0] for c in s]) for s in strings])) != 1: f.write('Case #'+str(case)+': Fegla Won\n')
	else:
		moves = 0
		strings = zip(*[[i[1] for i in s] for s in strings])
		for ints in strings:
			avg = min(ints, key=lambda x:abs(x-(sum(ints)/len(ints))))
			for i in ints:
				moves += abs(i-avg)
		f.write('Case #'+str(case)+': '+str(moves)+'\n')

	l += int(lines[l])+1
