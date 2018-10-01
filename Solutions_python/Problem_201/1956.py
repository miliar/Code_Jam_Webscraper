with open("input.txt","r") as file:
	lines=file.read().splitlines()
line_n=0
outlines=[]
t=int(lines[line_n])
line_n=line_n+1
for i in range(t):
	n,k=map(int,lines[line_n].split(" "))
	line_n=line_n+1
	filled=[0,n+1]
	for j in range(k):
		gap=-1
		pos=-1
		for l in xrange(len(filled)-1,0,-1):
			if(filled[l]-filled[l-1]-1>gap):
				gap=filled[l]-filled[l-1]-1
				pos=l-1
		mid = (filled[pos+1]+filled[pos])/2
		if(j==k-1):
			a = mid-filled[pos]-1
			b = filled[pos+1]-mid-1
			if(a>b):
				outlines.append("Case #"+str(i+1)+": "+str(a)+" "+str(b))
			else:
				outlines.append("Case #"+str(i+1)+": "+str(b)+" "+str(a)) 
			break
		filled.append(mid)
		filled.sort()
with open("output.txt","w") as file:
	for line in outlines:
		file.write(line+"\n")