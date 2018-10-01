def recycle(x):
	x = str(x)
	s = []
	k = 0
	while (k < len(x)):
		s.append(int(rotate(x, k)))
		k = k + 1
	return s

def rotate(x, y):
	s = x
	k = 0
	while (k < y):
		s = s + x[k]
		s = list(s)
		s.pop(0)
		s = ''.join(s)
		k = k + 1
	return s

f = open('C-small-attempt0.in.txt', 'r')
t = f.readline()
t = int(t)
g = open('B.out', 'w')

print t

x = 0
while (x < t):
	s = f.readline()
	s = s.split()
	a = int(s[0])
	b = int(s[1])
	y = a
	r = 0
	while (y <= b):
		s = recycle(y)
		for e in s:
			if ((e >= a) and (e <= b) and (e != y)):
				r = r + 1
		y = y + 1
	r = r/2
	r = str(r)
	r = 'Case #' + str(x+1) + ': ' + r
	if (x != t-1):
		r = r + '\n'
	g.write(r)
	x = x + 1
	
