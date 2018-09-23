#!/usr/bin/python
import sys

fi = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
fo = open(".".join(sys.argv[1].split('.')[:-1])+".out","w") if len(sys.argv) > 1 else sys.stdout

tc=int(fi.readline())
for i in range(1,tc+1):
	ln=fi.readline().split()
	N=int(ln[0])
	P=int(ln[1])

	ln=fi.readline().split()
	rcp=[]
	for n in range(N):
		rcp.append(int(ln[n]))

	pck=[]
	for n in range(N):
		ln=fi.readline().split()
		itm=[]
		for p in range(P):
			w=int(ln[p])
			max=int((w*10/9)/rcp[n])
			min=int((w*10/11)/rcp[n])+((w*10/11)%rcp[n]>0)
			if (min<=max):
				itm.append((min,max))
		itm.sort()
		pck.append(itm)
	
	cnt=0	
	if N==1:
		cnt=len(pck[0])
	else:	
		test=1
		while(test):
			min=0
			n = 0
			while(n<N):
				while(len(pck[n])):
					if pck[n][0][1] < min:
						pck[n].pop(0)
					else:
						if pck[n][0][0] > min:
							min = pck[n][0][0]
							n = -1
						break
				n+=1

			for n in range(N):
				if (len(pck[n])):
					pck[n].pop(0)
				else:
					test=0
			cnt+=test
		
			
					
	print("Case #{}: {}".format(i,cnt),file=fo)

