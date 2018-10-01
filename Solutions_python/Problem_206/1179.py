with open("input.txt","r") as file:
	lines=file.read().splitlines()
line_n=0
t= int(lines[line_n])
line_n=line_n+1
for i in range(t):
	d,n=map(int,lines[line_n].split(" "))
	line_n=line_n+1
	maxtime=0
	for j in range(n):
		k,s=map(int,lines[line_n].split(" "))
		line_n=line_n+1
		if ((d-k)/float(s)) > maxtime:
			maxtime=((d-k)/float(s))
	with open("output.txt","a") as file:
		file.write("Case #"+str(i+1)+": "+str(d/float(maxtime))+"\n")