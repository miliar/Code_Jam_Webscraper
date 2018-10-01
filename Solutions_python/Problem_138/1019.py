import fileinput

def deceitScore (n, k):
	score = 0
	for block in sorted(n):
		if block > min(k):
			score += 1
			del k[k.index(min(k))]
		else:
			del k[k.index(max(k))]
	return score

def warScore (n, k):
	score = 0
	for block in n:
		if block > max(k):
			score += 1
			del k[k.index(min(k))]
		else:
			del k[k.index(minAbove(k, block))]
	return score

def minAbove(l, above):
	mn = None
	for num in l:
		if num > above and (mn == None or num < mn):
			mn = num
	return mn

i = -1
N = []
for line in fileinput.input("codejam4.in"):
	i += 1
	if i == 0:
		continue
	if (i - 1) % 3 == 0:
		continue
	if (i - 1) % 3 == 1:
		N = line.split()
	if (i - 1) % 3 == 2:
		print("Case #" + str((i - 1) // 3 + 1) + ": " + str(str(deceitScore(N, line.split()))) + " " + str(warScore(N, line.split())))