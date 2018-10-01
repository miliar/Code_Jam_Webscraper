s = [item.rstrip('\n') for item in open('input.txt','r').readlines()]
numcases = int(s[0])
def main(index, case):
	num = int(s[index])
	na = (s[index+1].split())
	ke = (s[index+2].split())
	n = []
	k = []
	for i in na:
		n.append(float(i))
	for i in ke:
		k.append(float(i))
	n = sorted(n)
	k = sorted(k)
	#print n
	#print k
	wwin = 0
	min = 0
	cross = 1
	for f in n[::-1]:
		if f > k[num-cross]:
			wwin += 1
		else:
			cross += 1
	cross = 0
	for f in n:
		if f < k[cross]:
			min += 1
		else:
			cross += 1
	print 'Case #' + str(case) + ': ' + str(num-min) + ' ' + str(wwin)
for t in range(0,numcases):
	main(1+(3*t), t+1)