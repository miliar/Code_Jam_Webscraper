f = open('C0.table2')
num = []
for line in f.readlines():
	tup = eval(line)
	num.append(tup[1])
	if tup[1] == 4:
		num.append(9)
f.close()
# print len(num)
# print num[:10]
def biSearch(x):
	l = 0
	r = len(num)
	while l < r:
		m = (l + r) >> 1
		if num[m] < x:
			l = m + 1
		else:
			r = m
	return l

T = int(raw_input().split()[0])
for t in range(T):
	A, B = [int(i) for i in raw_input().split()]
	pA = biSearch(A)
	pB = biSearch(B+1)
	# print A, pA, B, pB
	print 'Case #%d: %d'%(t+1, pB-pA)

