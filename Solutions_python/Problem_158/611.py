import string

f=open('D-small-attempt2.in','r')
f1=open('out.txt','w')
T=string.atoi(f.readline(),10)
i=0
while i<T:
	line=f.readline()
	list=line.split(' ')
	x=int(list[0])
	r=int(list[1])
	c=int(list[2])
	rc=r*c
	if (rc/x*x)==rc:
		if r==1 or c==1:
			if x==3 or x==4:
				f1.write('Case #'+str(i+1)+': RICHARD\n')
			else:
				f1.write('Case #'+str(i+1)+': GABRIEL\n')
		elif r==2 or c==2:
			if x==4:
				f1.write('Case #'+str(i+1)+': RICHARD\n')
			else:
				f1.write('Case #'+str(i+1)+': GABRIEL\n')
		else:
			f1.write('Case #'+str(i+1)+': GABRIEL\n')
	else:
		f1.write('Case #'+str(i+1)+': RICHARD\n')
	i=i+1
f1.close()
f.close()