#!/usr/bin/python
import sys

fi = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
fo = open(".".join(sys.argv[1].split('.')[:-1])+".out","w") if len(sys.argv) > 1 else sys.stdout

TC=int(fi.readline())
for t in range(1,TC+1):
	
	N,K=map(int,fi.readline().split())
	U=float(fi.readline())
	Q=[]
	for q in fi.readline().split(): 
		Q.append(float(q))

	if N==K:
		Q.append(1.0)
		Q.sort()
		for k in range(K):
			if Q[k]<Q[k+1]:
				if ((k+1)*(Q[k+1]-Q[k]))<=U:
					U-=(k+1)*(Q[k+1]-Q[k])
					for i in range(k+1):
						Q[i]=Q[k+1]
				else:
					for i in range(k+1):
						Q[i]+=U/(k+1)
					break
		prob=1
		for k in range(K):
			prob=prob*Q[k]
	
	else:
		prob=-1
		
	print("Case #{}: {}".format(t,prob),file=fo)

