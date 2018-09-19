nums = dict ()

def incl (n):
	sn = str (n)
	for i in range (len (sn)):
		if sn [i] == '0':
			continue
		new = ""
		for j in range (len (sn)):
			new += sn [(i + j) % len (sn)]
		if n < int (new):
				nums [(n, int (new))] = True


for i in range (10, 1001):
	incl (i)

lines = open ("input.txt").read ().split ('\n')[:-1]
N = int (lines [0])

for i in range (1, N + 1):
	stuff = lines [i].split (' ')
	A, B = int (stuff [0]), int (stuff [1])
	total = 0
	for key in nums.keys ():
			if key [0] >= A and key [1] <= B:
				total += 1
	print "Case #%d: %d" % (i, total)
