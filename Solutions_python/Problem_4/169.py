import sys
infile=open('A-large.in')
T=int((infile.readline()).rstrip())
#print "No of Test Cases: "+str(nooftestcases)
i=1
while i<=T :
	#Input Sequence
	n=int((infile.readline()).rstrip())
	j=0
	v1=[]
	v2=[]
	v1=(infile.readline()).rstrip().split(' ')
	v1=[int(x) for x in v1] 
	v2=(infile.readline()).rstrip().split(' ')
	v2=[int(x) for x in v2]
	v1.sort()
	v2.sort()
	v2.reverse()
	k=0
	while j<n :
		k+=v1[j]*v2[j]
		j+=1
	print 'Case #'+str(i)+': '+str(k)
	i+=1

