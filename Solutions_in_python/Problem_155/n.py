T  = int(raw_input())
i = 1

while i<=T:
	#Problem Start
	line = raw_input()
	s = line.split()
	Smax=int(s[0])
	P=s[1]

	sum = 0
	need = 0
	j = 0
	for s in P:
		if j > sum:
			need=need+(j-sum)
			sum=sum+(j-sum)
		sum=sum+int(s)
		j=j+1

	#Print
	print "Case #%d: %d" % (i,need)

	#End
	i=i+1

