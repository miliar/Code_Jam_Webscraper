#! /usr/bin/env python2.7


T=int(raw_input())
for test in xrange(1,T+1):
	n=int(raw_input())
	stglist=[]
	for i in xrange(n):
		newstring=raw_input()
		stglist.append(list(newstring.strip()))
	countlist=[]
	for i in xrange(n):
		j=0
		countlist.append([])
		countlist[-1].append(1)
		while(j<len(stglist[i])-1):
			if (stglist[i][j]==stglist[i][j+1]):
				stglist[i].pop(j)
				countlist[-1][-1]+=1
			else :
				countlist[-1].append(1)
				j+=1
	flag=True
	i=0
	while(flag and i<n-1 ):
		if stglist[i]==stglist[i+1]:
			i+=1
		else :
			flag=False
	if flag:
		minlength=len(stglist[0])
		somme=[round((float(sum(colon)))/n) for colon in zip(*countlist)]
		total_moves=0
		for j in xrange(minlength):
			for i in xrange(n):
				total_moves+=int(abs(countlist[i][j]-somme[j]))
		print "Case #{}: {}".format(test, total_moves)
			
	else :
		print "Case #{}: Fegla Won".format(test)