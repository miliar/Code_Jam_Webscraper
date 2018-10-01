fp=open("B-large.in","r")
ptr=open("output.txt","w")
num_cases=int(fp.readline())
for i in range(num_cases):
	list1=fp.readline().split()
	c,f,x=map(float,list1)
	#print c,f,x
	time=0
	current_rate=2
	while 1:
		time1=float(x/current_rate)
        	time2=float(c/current_rate) + float(x/(current_rate+f))
		if time2>time1:
			time+=float(x/current_rate)
			break
		else:
			time+=float(c/current_rate)
			current_rate+=f
	ptr.write("Case #{}: {}\n".format(i+1,time))
