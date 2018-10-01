#!usr/bin/python

f=open("C-small-attempt3.in",'r')
cases = int(f.readline())
rawdata=[]
for line in f:
	if line != '':
		rawdata.append(line.rstrip().split(' '))
f.close()

data=[]
for i in range(0, cases):
	a=rawdata[i*2]
	b=rawdata[(i*2)+1]
	times = int(a[1])
	string = b[0]*times
	data.append(string)

#print data

source = ['11','1i','1j','1k','i1','ii','ij','ik','j1','ji','jj','jk','k1','ki','kj','kk']
mult = ['1','i','j','k','i','-1','k','-j','j','-k','-1','i','k','j','-i','-1']
match='ijk'

def multiply(x):
	if x[0]=='-':
		y=x[1:]
	else:
		y=x
	i=source.index(y)
	j=mult[i]
	#print j
	if x[0]!='-':
		return j
	else:
		if j[0]=='-':
			return j[1:]
		else:
			return '-'+j
	
	
		
		
#print multiply('-ji')	

def big_mul(st):
	if len(st)==1:
		return st
	while True:
		temp=st[:2]
		if temp[0]=='-':
			temp=st[:3]
		an=multiply(temp)
		st=st.replace(temp,an,1)
		#print temp, an, st, type(st)
		if st[0]=='-' and len(st)==2:
			break
		if len(st)==1:
			break
	return st
#print big_mul('jijijijijiji')

def check(s0):
	l=len(s0)
	for i in range(1,l-2):
		s1=s0[:i]
		if big_mul(s1)=='i':
			#print 'ok i', s1
			for j in range(i+1,l-1):
				s2=s0[i:j]
				if big_mul(s2)=='j':
					#print 'ok j', s2
					s3=s0[j:l]
					#print s3, big_mul(s3)
					if big_mul(s3)=='k':
						#print 'ok k'
						return 1
	return 0
						
#print check('jijijijijiji')	

g=open("outC.txt", 'w')

for i in range(len(data)):
	each=data[i]
	print i
	ans=''
	#print big_mul(each)
	if len(each)<3:
		ans='NO'
		#print 1
	if len(each)==3:
		if each=='ijk':
			ans = 'YES'
			#print 2
		else:
			ans = 'NO'
			#print 3
	if len(each)>3:
		num1=each.count(each[0])
		if big_mul(each)=='-1':
			if num1!=len(each):
				if check(each)==1:
					ans='YES'
				else:
					ans='NO'
			else:
				ans='NO'
		else:
			ans='NO'
	answer = "Case #"+str(i+1)+": "+ans
	print>>g, answer

g.close()		
