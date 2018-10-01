fin = open("B-small-attempt0.in", "rb")
count = int(fin.readline())
fout = open("b-out.txt", "wb")

for i in range(1, count + 1):
	arr = [int(x) for x in fin.readline().split()]
	S = arr[1]
	p = arr[2]
	scores = arr[3:]

	if (p - 1) * 2 > 0:
		minNormal = p + (p - 1) * 2
	else:
		minNormal = p

	if (p - 2) * 2 > 0:
		minSurprize = p + (p - 2) * 2
	else:
		minSurprize = p

	res = 0
	for score in scores:
		if score >= minNormal:
			res += 1
		elif score >= minSurprize and S:
			S = S - 1
			res += 1
	fout.write("Case #%d: %d\n" % (i, res))

fin.close()
fout.close()

