
def solve(t):
	r1=int(raw_input())
	dic={}
	grid1=[]
	for i in xrange(4):
		grid1.append([int(el) for el in raw_input().split()])

	ans = 0

	r2 = int(raw_input())

	grid2=[]

	for i in xrange(4):
		grid2.append([int(el) for el in raw_input().split()])
		if i==(r2-1):
			for k in xrange(4):
				if grid2[i][k] in grid1[r1-1]:
					if ans!= 0:
						ans = -1
					else:
						ans=grid2[i][k]

	if ans>0:
		print "Case #%d: %d"%(t,ans)
	elif ans<0:
		print "Case #%d: Bad magician!"%t 
	else:
		print "Case #%d: Volunteer cheated!"%t 







t=int(raw_input())

for i in xrange(t):
	solve(i+1)



