din = open('small.in','r')
dout = open('small.out','w')

T = int(din.readline())
tag = ['R', 'O', 'Y', 'G', 'B', 'V']
d = {
	'R':['G', 'Y', 'B','#'],
	'O':['G', 'B', '#'],
	'Y':['V', 'R', 'B', '#'],
	'G':['R', 'O', '#'],
	'B':['O', 'R', 'Y', '#'],
	'V':['Y', '#']
}

for K in range(1,T+1):
	line = list(din.readline().split())
	N = int(line[0])
	R = int(line[1])
	O = int(line[2])
	Y = int(line[3])
	G = int(line[4])
	B = int(line[5])
	V = int(line[6])

	r = ['R']*R
	o = ['O']*O
	y = ['Y']*Y
	g = ['G']*G 
	b = ['B']*B 
	v = ['V']*V 
	source = []
	source.extend(r)
	source.extend(o)
	source.extend(y)
	source.extend(g)
	source.extend(b)
	source.extend(v)
	res = ['#','#']
	res.insert(1,source[0])
	source.remove(source[0])
	i = 0
	while len(source) > 0 and i < len(source):
		L = len(source)
		tmp = source[i]
		neighbor = d[tmp]
		for j in range(1, len(res)):
			if res[j] in neighbor and res[j-1] in neighbor:
				res.insert(j, tmp)
				source.remove(tmp)
				break
		if len(source) != L:
			i = 0
			continue
		else:
			i += 1
	print K
	if res[-2] not in d[res[1]] or len(source) > 0:
		dout.write('Case #%d: %s\n' % (K, 'IMPOSSIBLE'))
	else:
		dout.write('Case #%d: %s\n' % (K, ''.join(res[1:-1])))



din.close()
dout.close()




