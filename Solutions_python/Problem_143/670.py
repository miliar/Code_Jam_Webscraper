# your code goes here
f=open('in.txt','r')
g=open('outAND.txt','w')
#lines=f.readlines[1:]
import sys
lines=f.readlines()[1:]
pairs=0
tt=0
for i in xrange(0,len(lines)):
        tt+=1
	pairs=0
	a,b,k=[int(i) for i in lines[i].split()]
	for i in xrange(0,a):
		for j in xrange(0,b):
			if i&j <k:
				pairs+=1
	g.write(("Case #%d: %d\n")%(tt,pairs))
g.close()
