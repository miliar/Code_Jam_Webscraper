def check(n):
	for i in xrange(0, len(n)-1):
		if n[i] > n[i+1]:
			return False
	return True
f = open('B-small-attempt1.in')
o = open('output.out', 'w')
t = int(f.readline().strip())
for i in xrange(1, t + 1):
	n = f.readline().strip()
	'''ans = ''
	tt = 0
	if check(n):
		ans = n
	else:
		for j in xrange(0, len(n)):
			if int(n[len(n)-j-1]) == 0 or j == 0 or (int(n[len(n)-j-1]) == 1 and tt and j != len(n)-1):
				ans = str(9) + ans
				tt = 1
			elif int(n[len(n)-j-1]) != 1 and tt:
				ans = str(int(n[len(n)-j-1])-1) + ans
				tt = 0
			elif not tt:
				ans = str(min(int(n[len(n)-j-1])), int(n[len(n)-j-2])) + ans'''
	while not check(n):
		n = str(int(n)-1)
	o.write("Case #{}: {}\n".format(i, n))
