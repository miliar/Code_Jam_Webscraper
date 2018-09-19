#!/usr/bin/python
import os
from collections import deque


def step(m,s,bm,bs):
	t=abs(m-bm)+1
	m=bm
	ds=max(abs(s-bs)-t,0)
	if s-bs>0:
		s=bs-ds
	else:
		s=bs+ds
	return m,s,t

def calc(O,B,S):
	time = 0
	o=1
	b=1
	oo=1
	if len(O)>0:
		oo=O.popleft()
	bb=1
	if len(B)>0:
		bb=B.popleft()
	while len(S)>0: 
		c=S.popleft()
		if c=='O':
			m,s,t = step(o,b,oo,bb)
			print 'O',o,b,oo,bb,m,s,t
			time+=t
			o=m
			b=s
			if len(O)>0:
				oo=O.popleft()
		else:
			m,s,t = step(b,o,bb,oo)
			print 'B',o,b,oo,bb,m,s,t
			time+=t
			o=s
			b=m
			if len(B)>0:
				bb=B.popleft()
	return time

























for fn in os.listdir('.'):
	if fn.rfind("in")!=-1:
		fnn=fn
		break
print "reading file",fnn
f=open(fnn,"r")
fw=open(fnn+".out",'w')
line=f.readline().split()
T=int(line[0])
for i in range(T):
	line=f.readline().split()
	N=int(line[0])# No buttons
	O=deque()
	B=deque()
	S=deque()
	print line
	for j in range(N):
		jj = 1+ j*2
		S.append(line[jj])
		if line[jj]=='O':
			O.append(int(line[jj+1]))
		else:
			B.append(int(line[jj+1]))
	print 'O:',O
	print 'B:',B
	print 'S:',S
	r=calc(O,B,S)
	print 'vysledok',r
	fw.write("Case #"+str(i+1)+": "+str(r)+"\n")
f.close()
fw.close()
print "done"