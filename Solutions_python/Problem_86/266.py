lines=[]
file = open('C3.in','r')
allLines = file.readlines()
file.close()
for line in allLines:
	a = line.split()
	lines.append(a)

N=int(lines[0][0])

def fn(n,l,h,freq):
	#print 'n,l,h',n,l,h
	if l<=1:
		return 1
	else:
		b=int(min(freq))
		#print 'b',b
		lists=[]
		i=1
		'''if b<>1:
			while 1:
				c=int(b)*int(i)
				i+=1
				#print 'c,h',c,h
				if c<=h and c>=l:
					#print 'here,c',c
					lists.append(c)
				if int(c)>int(h):
					#print 'breaks'
					break
			#print lists	
		else:'''
		lists=range(l,h+1)
			#print lists
		for i in lists:
			flag=0
			for j in range(n):
				f=int(freq[j])
				if f%i==0 or i%f==0:
					continue
				else:
					flag=1
					break
			if flag==0:
				return i
			elif flag==1:
				continue
		return -1		
for count in range(1,N+1):
	flag=0
	seq=lines[2*count-1]
	n=int(seq[0])
	l=int(seq[1])
	h=int(seq[2])
	freq=lines[2*count]		#gives all of the integers 
	#print 'candies',candies
	ints=[int(freq[i]) for i in range(n)]
	#print ints
	a=fn(n,l,h,freq)
	if a==-1:
		print 'Case #%d:' % (count),'NO'
	else:
		print 'Case #%d:' % (count),a
