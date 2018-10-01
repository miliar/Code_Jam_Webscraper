#!/usr/bin/python

f=open("A-small-attempt0.in",'r')
out=open("output.txt",'w+')
n=int(f.readline())
for i in range(0,n):
	row=int(f.readline())
	for p in range(1,5):
		if (p==row):
			choice1=f.readline().split()
		else:
			f.readline()
	row=int(f.readline())
	for p in range(1,5):
		if (p==row):
			choice2=f.readline().split()
		else:
			f.readline()
	num = len(list(set(choice1) & set(choice2)))
	if(num==1):
		out.write("case #"+str(i+1)+": "+str(list(set(choice1) & set(choice2))[0]+"\n"))
	if(num>1):
		out.write("case #"+str(i+1)+": Bad magician!\n")
	if(num==0):
		out.write( "case #"+str(i+1)+": Volunteer cheated!\n")

f.close()
out.close()
