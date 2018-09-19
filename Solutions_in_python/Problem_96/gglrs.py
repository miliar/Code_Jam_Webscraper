import sys
t=input()
i=0
tmp=[]
for i in range(t):
	inp=raw_input().split()
	n=int(inp[0])
	sur=int(inp[1])
	p=int(inp[2])

	if p==0:cmp1=cmp2=0
	elif p==1:cmp1=cmp2=1
	else:
		cmp1=(3*int(p)-4)
		cmp2=(3*int(p)-2)

	k=bet=betOnlyIfSur=0
	for s in inp[3:]:
		if int(s)<cmp1:continue
		else :
			bet+=1
			if int(s)<cmp2:
				betOnlyIfSur+=1		
	final=bet
	if(betOnlyIfSur-sur>0):
		final=bet-(betOnlyIfSur-sur)
	sys.stdout.write('Case #'+str(i+1)+': '+str(final)+'\n')
	
