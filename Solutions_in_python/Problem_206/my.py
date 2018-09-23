inFile = open("A-large.in")
outFile = open("result.out", "w")
x=[]
for line in inFile:
	x.append(line)
t =int(x[0])
y=0
for i in range(t):
	#y+=1
	#r,c =map(int,x[y].strip().split())
	#a=[]
	#for z in range(r):
		#y+=1
#a.append(list(x[y].strip()))
	y+=1
	d,n=map(int,x[y].strip().split(" "))
	
	b=[]
	max=0.0
	l=0
	for k in range(n):
		y+=1
		b.append(map(float,x[y].strip().split(" ")))
		t=(d-b[k][0])/b[k][1]
		print t
		if t>max:
			max=t
		"""if l==0:
			if k==0:
				t=(d-b[0][0])/b[0][1]
			else:
				if t>(d-b[1][0])/b[1][1] :
					l=1

				else:
					t=(d-b[1][0])/b[1][1]
					b.pop(0)
	#print b"""
	
	print max
	
	outFile.write("Case #"+str(i+1)+": "+str(d/max)+"\n")
	
	#outFile.write("Case #"+str(i+1)+": "+str(int("".join(n)))+"\n")
	
inFile.close()
outFile.close()
