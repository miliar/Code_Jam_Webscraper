def snapper (a):
	i = 0
	while i<len(a)and(a[i]==1):
		a[i]=0
		i+=1
	if i <len(a):
		a[i] = 1
	return a

def check(c,k):
	if k == 1:
		if c[k-1] == 0:
			return False
		else:
			return True
	else:
		if c[k-1] == 0:
			return False
		else: 
			return check(c,k-1)
			

def snap(b, k):
	i = 1
	length = len(b)
	while (i <= k):	
		
		b = snapper(b)
		i+=1
		
		if check(b,length):
			if (k+1)%i==0:
				return "ON"
			else:
	
				return "OFF"
	return "OFF"

def testLine(n):
	f = file.readline()
	a=""
	b=""
	inA = True
	for i in f:
		if inA == True and i!=" ":
			a+=i
		else:
			inA = False
		if inA == False and i!=" ":
			b+=i
	a=int(a)
	b=int(b)
	list=[]
	for i in range(0,a):
		list+=[0,]
	outputfile.write("Case #"+str(n)+": "+snap(list,b)+"\n")
	
	
file=open("A-small-attempt2.in","r")
outputfile=open("output.txt","w")
counter = int(file.readline())
for i in range(1,counter+1):
	testLine(i)


		
	