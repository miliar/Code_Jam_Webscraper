#encoding: utf-8

t = int(raw_input())

for case in range(t):
	c = raw_input().split()[1]

	needed = 0
	shyness = 0
	standing = 0
	for i in c:
		persons = int(i)
		if shyness > standing:
			needed += shyness - standing
			standing = shyness

		standing += persons
		shyness += 1
	print 'Case #'+str(case+1)+': '+str(needed)
