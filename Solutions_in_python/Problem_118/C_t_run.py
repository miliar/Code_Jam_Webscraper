goodnumbers=map(int,open('C.data').read().splitlines())
goodnumbers=sorted(list(set(goodnumbers)))
T=int(raw_input())
for case in xrange(T):
	A,B=map(int,raw_input().split())
	#print [i for i in goodnumbers if i>=A and i<=B]
	beg=0
	while goodnumbers[beg]<A:
		beg+=1
	end=beg-1
	while goodnumbers[end+1]<=B:
		end+=1
	ret=end-beg+1
	print 'Case #%d:'%(case+1),ret
