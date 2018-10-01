fairpair = []
MAXSQ = 10**7 +1

def checkpal(a):
	s = str(a)
	if (s == s[::-1]):
		return True
	return False

for i in range(MAXSQ):
	if checkpal(i) and checkpal( i**2 ):
		fairpair.append(i**2)

#for i in range(20):
#	print fairpair[i]

f = open('C.out', 'w')

T = input()
for i in range(T):
	a = raw_input()
	a = a.split(' ')
	a[0] = int(a[0])
	a[1] = int(a[1])
	lower = 0
	upper = len(fairpair)

	#BS on lower bound
	d = 0
	while( lower < upper -1):
		d = (lower+upper)/2
		#print lower, upper, d, fairpair[d], a[0]
		if fairpair[d] >= a[0]:
			upper = d
		elif fairpair[d] < a[0]:
			lower = d

	limd = lower

	lower = 0
	upper = len(fairpair)
	while( lower < upper -1):

		d = (lower+upper)/2

		if fairpair[d] > a[1]:
			upper = d
		elif fairpair[d] <= a[1]:
			lower = d

	limu = upper
	#print limd, limu
	f.write("Case #"+str(i+1)+": "+str(limu - limd -1)+"\n")