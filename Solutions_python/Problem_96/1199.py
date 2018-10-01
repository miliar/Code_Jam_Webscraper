f = open('B-large.in','r')
#output = open('B-small.out','w')

NumberOfCases = int(f.readline())
CaseNumber = 1
for i in range(NumberOfCases):
	ans = 0
	a = [int(j) for j in f.readline().split()]
	T = a[0]
	Surp = a[1]
	p = a[2]
	score = a[3:]
	for SumScore in score:
		SumTwo = SumScore - p
		if SumTwo >= max(2*(p-2),0):
			if SumTwo >= max(2*p-2,0):
				ans = ans + 1
			elif SumTwo == (2*p - 3) or SumTwo == (2*p - 4):
				if Surp > 0:
                                        ans = ans + 1
					Surp = Surp - 1
	value = 'Case #{}: {}'.format(CaseNumber,ans)
	CaseNumber = CaseNumber + 1
	print value
	#output.write(value)		


