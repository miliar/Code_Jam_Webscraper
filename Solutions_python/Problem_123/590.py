def doub (me, big):
	addends = []

	while me <= big:
		addends.append(me - 1)
		me += me - 1

	return addends

size = "small"
attempt = "1"

f = open("A-{}-attempt{}.in".format(size, attempt), "r")
out = file("{}{}.out".format(size, attempt), "w")

lines = f.read().splitlines()[1:]

cases = []
output = []

for i in range(0, len(lines), 2):
	cases.append((int(lines[i].split(" ")[0]), sorted(map(int, lines[i+1].split(" ")))))

for case in cases:
	size = case[0]
	blobsLeft = case[1]
	ops = 0

	while len(blobsLeft) != 0:
		print size, blobsLeft
		if size == 1:
			blobsLeft.pop(0)
			ops += 1
			continue

		d = doub(size, blobsLeft[0])

		if blobsLeft[0] < size:
			size += blobsLeft.pop(0)
		elif len(d) < len(blobsLeft):
			blobsLeft = d + blobsLeft
			ops += len(d)
		else:
			blobsLeft.pop(0)
			ops += 1

	output.append(ops)

for outNum in range(len(output)):
	out.write("Case #{0}: {1}\n".format(outNum + 1, output[outNum]))