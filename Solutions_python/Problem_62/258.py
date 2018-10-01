#!/usr/bin/python
import os
for fn in os.listdir('.'):
	if fn.rfind("in")!=-1:
		fnn=fn
		break
def inn(x,a):
	Ax=a[1]*x + a[0] 
	Ba=min(a[0],a[2])
	Bb=max(a[0],a[2])
	return (Ax>=Ba and Ax<=Bb)
	
def intersect(a,b):
	if a[1] == b[1]:
		return False
	x = float(b[0]-a[0])/float(a[1]-b[1])
	if (inn(x,a) and inn(x,b)):
		return True
	else:
		return False

print "reading file",fnn
f=open(fnn,"r")
fw=open(fnn+".out",'w')
line=f.readline().split()
T=int(line[0])
for Case in range(T):
	result=0
	N = int((f.readline().split())[0])
	Ls=[]
	for i in range(N):
		AB=f.readline().split()
		Ai = int(AB[0])
		Bi = int(AB[1])
		t=(Ai,Bi-Ai,Bi)
		for j in Ls:
			if intersect(t,j):
				result+=1
		Ls.append(t)
	fw.write("Case #"+str(Case+1)+": "+str(result)+"\n")
