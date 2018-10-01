T = input()
for i in xrange(T):
	r1 = input()
	for j in xrange(4):
		if j+1 == r1:
			arr1 = [k for k in raw_input().split()]
		else:
			raw_input()
	r2 = input()
	for j in xrange(4):
		if j+1 == r2:
			arr2 = [k for k in raw_input().split()]
		else:
			raw_input()
	res = list(set(arr1) & set(arr2))
	l = len(res)
	prefix = "Case #%d: "%(i+1)
	if l > 1:
		print prefix + "Bad magician!"
	elif l == 0:
		print prefix + "Volunteer cheated!"
	else:
		print prefix + res[0]

