T=input()
flip = lambda x:(x+1)%2
for x in range(T):
	inp=raw_input().split(' ')
	S = inp[0]
	length=len(S)
	k= int(inp[1])
	n=[]
	for y in S:
		if y=='+':
			n.append(1)
		else:
			n.append(0)

	K = int(inp[1])
	if S.count('+')==len(inp[0]):
		print "Case",'#'+str(x+1)+':',0
	else:
		cnt=0
		for z,y in enumerate(n):
			if y==0 and z+k<length+1:
				n[z:z+k]=map(flip,n[z:z+k])
				cnt+=1
		
		if sum(n)==length:
			print "Case",'#'+str(x+1)+':',cnt
		else:
			print "Case",'#'+str(x+1)+':',"IMPOSSIBLE"

					
	
		
		
	
