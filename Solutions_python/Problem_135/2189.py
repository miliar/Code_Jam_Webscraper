def ints():
    return map(int, raw_input().split())

t=int(raw_input())
for tt in range(t):
	x = int(raw_input())
	vals=[]
	for i in range(4):
		vals.append(ints())
	y = int(raw_input())
	vals2=[]
	for i in range(4):
		vals2.append(ints())
	cnt =0
	res = -1
	for i in range(4):
		for j in range(4):
			if vals[x-1][i] == vals2[y-1][j]:
				 cnt+=1
				 res=vals[x-1][i]
	if cnt==1:
		print 'Case #%d: %d'%(tt+1,res)
	if cnt>1:
		print 'Case #%d: Bad magician!'%(tt+1)
	if cnt==0:
		print 'Case #%d: Volunteer cheated!'%(tt+1)