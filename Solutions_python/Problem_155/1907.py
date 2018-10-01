#!usr/bin/python

f=open("A-small-attempt0.in",'r')
cases = int(f.readline())
data=[]
for line in f:
	if line != '':
		data.append(line.rstrip().split(' '))
print data
f.close()

g=open('out1.txt','w')

for i in range(len(data)):
	each=data[i]
	ans = 0
	mx = int(each[0])
	aud = each[1]
	for x in range(1,mx+1):
		want=x
		have=0
		for y in range(0,x):
			have+=int(aud[y])
		#print want, have, ans
		if (have+ans)-want<0:
			ans+=(want-(have+ans))
	print ans
	answer="Case #"+str(i+1)+": "+str(ans)+'\n'
	g.write(answer)

g.close()
