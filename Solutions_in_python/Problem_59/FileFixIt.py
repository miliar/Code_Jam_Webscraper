import util

def FileFixIt(N,M,paths):
	pc = []
	t,i = 0,1
	for p in paths:
		x = ''
		for y in p.split('/')[1:]:
			x = "%s/%s" % (x,y)
			if x not in pc:
				pc.append(x)
				if i > N:
					t += 1
		i += 1
	return t

#test = util.dotest('A-small-attempt0')
test = util.dotest('A-large')
y = 0
for i in test.T:
	N,M = map(int,test.fi[y].split(' '))
	y += 1
	test.y( FileFixIt(N,M,test.fi[y:y+N+M]) )
	y += N+M
