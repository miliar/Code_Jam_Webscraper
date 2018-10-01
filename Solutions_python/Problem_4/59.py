from sys import stdin, stdout
cin=open("in")
cout=open("out","w")
n_cases=int(cin.readline().rstrip())
for case_i in xrange(1,n_cases+1):
	dim=int(cin.readline().rstrip())
	v1=map(int, cin.readline().split(" "))
	v2=map(int, cin.readline().split(" "))
	v1.sort()
	v2.sort()
	#print v1
	#print v2
	sum=0
	for i in xrange(dim):
		sum+=v1[i]*v2[-i-1]
	cout.write("Case #"+str(case_i)+": "+str(sum)+"\n")

