def find_locs(search, target):
	ret = []
	pos = 0
	while not search.find(target, pos) == -1:
		temp = search.find(target, pos)
		ret.append(temp)
		pos = temp+1
	return ret

def check_recycle(a, b):
	A = str(a)
	B = str(b)
	ret = 0
	locs = find_locs(B, A[0])
	# print str(a) + " " + str(b)
	# print locs
	for start in locs:
		success = 1
		for i in range(0, len(A)):
			if not A[i] == B[(i+start)%len(A)]:
				success = 0
				break
		if success == 1:
			ret = 1
			break
	return ret

def recycled_pairs(a, b):
	ret = 0
	for i in range(a+1, b+1):
		for j in range(a, i):
			ret += check_recycle(i, j)
	return ret

filein = open('./C-small-attempt0.in', 'r')
fileout = open('./C-small-attempt0.out', 'w')
lines = filein.readlines()

data = {}
for i, line in enumerate(lines):
	if not i == 0:
		temp = line.split(' ')
		a = int(temp[0])
		b = int(temp[1])
		data[i] = recycled_pairs(a, b)

for key in data:
	fileout.write("Case #" + str(key) + ": " + str(data[key]) + "\n")

filein.close()
fileout.close()