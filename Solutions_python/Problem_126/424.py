import fileinput

fi = fileinput.input()
T = int(fi.readline())

for caseN in xrange(T):
	name,n = fi.readline().strip().split()
	n=int(n)
	target = 'c'*n
	code=''
	for l in name:
		if l in 'aeiou': code+='v'
		else: code+='c'
	answer=0
	for ind1 in xrange(len(name)):
		for ind2 in xrange(ind1+1,len(name)+1):
			substr = code[ind1:ind2]
			if target in substr:
				answer+=1
	print 'Case #'+str(caseN+1)+': '+str(answer)
