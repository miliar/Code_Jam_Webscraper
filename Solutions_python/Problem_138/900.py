from collections import deque
import bisect

t=input()
for x in range(1,t+1):
	N = input()
	a=raw_input()
	Naomi=[float(y) for y in a.strip().split()];
	a = raw_input()
	Ken=[float(y) for y in a.strip().split()];
	
	Naomi.sort()
	N1 = deque(Naomi)
	Ken.sort()
	K1 = deque(Ken)
	dwpoints=0
	wpoints=0
	for i in range(0,N):
		if N1[0] < K1[0] :
			N1.popleft()
			K1.pop()
		else:
			N1.popleft()
			K1.popleft()
			dwpoints = dwpoints +1
	
	for n1 in Naomi:
			k=bisect.bisect(Ken,n1)
			if k < len(Ken):
				Ken.pop(k)
			else:
				wpoints = wpoints+1
	
		
	print "Case #"+str(x)+": "+str(dwpoints)+" "+str(wpoints)
