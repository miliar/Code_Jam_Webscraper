#!/usr/bin/python

fin = open('B-large.in')
fout = open('b.out', 'w')
num = int(fin.readline())
l=1
v=[[],[]];

def route(a, flag, n, minN):
	if flag == 'x':
		r = a[n]
	elif flag == 'y':
		r = [i[n] for i in a]
	b = 101
	for j in r:
		if (not j == 101) and (not j == minN):
			return 0
	global v
	if flag == 'x':
		for j in xrange(len(a[n])):
			a[n][j] = 101
		v[0][n] = 1
	else:
		for j in xrange(len(a)):
			a[j][n] = 101
		v[1][n] = 1
	return 1

def check(a, h, l):
	global v
	minx = []
	for x in a:
		minx.append(min(x))
	minN = min(minx)
	if minN == 101:
		return 1
	for i in xrange(h):
		if (a[i][0] == minN or (a[i][0] == 101 and v[0][i] == 0)) and route(a, 'x', i, minN):
			return check(a, h, l)

	for j in xrange(l):
		if (a[0][j] == minN or (a[0][j] == 101 and v[1][j] == 0)) and route(a, 'y', j, minN):
			return check(a, h, l)
	return 0

while(l<=num):
	h, j = fin.readline().split('\n')[0].split(' ')
	a = []
	h = int(h)
	j = int(j)
	n = 0;
	v = [[],[]]
	while n<h:
		a.append(fin.readline().split('\n')[0].split(' '))
		n += 1
	for i in xrange(h):
		v[0].append(0)
		for k in xrange(j):
			a[i][k] = int(a[i][k])
	for m in xrange(j):
		v[1].append (0)
	pre = 'Case #'+str(l)+': '
	if check(a, h, j):
		fout.write(pre + 'YES\n')
	else:
		fout.write(pre + 'NO\n')
	l += 1