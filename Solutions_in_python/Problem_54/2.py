def gcd(a,b):
	while not a%b == 0:
		temp = a%b
		a = b
		b = temp
	return b
		

#def sortList(a):
#	a=set(a)
#	if len(a) == 2:
#		a=sorted(a)
#		return a[1]-a[0]
#	b=[]
#	c=a
#	a=sorted(a)
#	while len(a)>2:
#		for i in range(1,len(a)):
#			b+=[(a[i]-a[i-1]),]
##			
#		a=sorted(set(b))
#		b=[]
#	if len(a)==1:
#		result = a[0]
#	else:
#		result=gcd(a[1],a[0])
#	if result == 1:
#		return -1
#	else:
#		return result  

def sortList(a):
	a=sorted(set(a))
	b=[]
	for i in range(1,len(a)):
		b+=[(a[i]-a[i-1]),]
	b=sorted(set(b))
	temp = b[0]
	for i in range(1,len(b)):
		temp = gcd(temp,b[i])
	return temp

def testLine(n):
	f = file.readline()
	inAword = False
	isCounter=True
	counter = ""
	b=""
	c=[]
	for i in f:
		if i!=" " and isCounter == True:
			counter+=i
		else:
			isCounter = False
		if isCounter==False:
			if i == " ":
				if b !="":
					c+=[int(b),]
				b=""
				
			else:
				b+=i
	c+=[int(b),]
	
	number = sortList(c)
	if number ==1:
		outputfile.write("Case #"+str(n)+": "+str(0)+"\n")
	elif c[0]%number == 0:
		outputfile.write("Case #"+str(n)+": "+str(0)+"\n")
	else:
		outputfile.write("Case #"+str(n)+": "+str(number-c[0]%number)+"\n") 
		
		
file=open("B-large.in","r")
outputfile=open("output2.txt","w")
counter = int(file.readline())
for i in range(1,counter+1):
	testLine(i)

