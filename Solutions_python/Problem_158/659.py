f=open("D-small-attempt2.in","r")
f2=open("output2.out", "w")
data=f.read().splitlines()
c=int(data[0])
line=1
result=""
for i in range(c):
	#print i+1
	temp=data[line].split(" ")
	#print temp
	line+=1
	x=int(temp[0])
	r=int(temp[1])
	c=int(temp[2])
	#check 1
	if r*c % x==0:
		if x==1 or x==2:
			if r*c >= x:
				result+="Case #"+str(i+1)+": "+"GABRIEL"+"\n"
				#print "GABRIEL"
			else:
				result+="Case #"+str(i+1)+": "+"RICHARD"+"\n"
				#print "RICHARD"
		else:
			if r*c > x:
				if min(r,c) > float(x/2):
					result+="Case #"+str(i+1)+": "+"GABRIEL"+"\n"
					#print "GABRIEL"
				else:
					result+="Case #"+str(i+1)+": "+"RICHARD"+"\n"
					#print "RICHARD"
			else:
				result+="Case #"+str(i+1)+": "+"RICHARD"+"\n"
				#print "RICHARD"
	else:
		result+="Case #"+str(i+1)+": "+"RICHARD"+"\n"
		#print "RICHARD"
#print result
f2.write(result)
f2.close()
