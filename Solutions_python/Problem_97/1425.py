def inRange(n, A, B):
	if n >= A and n <= B and d[n] != 0:
		return True
	return False


f = open('input.txt')
t = int(f.read(2))
case = 1
for i in f:
	try:
		A, B = i.split(" ")
	except:
		print i
		continue
	A, B = int(A), int(B)
	d = {}
	pairs = []
	count = 0
	for i in range(A, B + 1):
		d[i] = i
	for i in d:
		if d[i] == 0:
			continue
		x = i
		x = [j for j in list(str(x))]
		for j in range(1, len(str(i)) + 1):
			x = x[j:] + x[:j]
			temp = int(''.join(x))
			while temp != i:
				if inRange(temp, A, B):
					#d[int(''.join(x))] = 0
					if (temp, i) not in pairs and (i, temp) not in pairs:
						count += 1
					pairs.append((temp, i))
				x = x[j:] + x[:j]
				temp = int(''.join(x))
	print "Case #%d: %d" % (case, count)
	case += 1