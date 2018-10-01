def getLine(l):
	lines=[]
	for i in range(4):
		lines.append(map(int,raw_input().split(" ")))
	return lines[l-1]

def magic(caZe):
	print "Case #"+str(caZe)+":",
	r1=input()
	digs1=getLine(r1)
	r2=input()
	digs2=getLine(r2)
	res=[]
	for dig in digs1:
		if dig in digs2:
			res.append(dig)
	if len(res)==1:
		print res[0]
	elif len(res)==0:
		print "Volunteer cheated!"
	else:
		print "Bad magician!"
	#print digs1,"potato",digs2
casez=input()
for i in range(casez):
	magic(i+1)
