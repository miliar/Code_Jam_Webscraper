import sys

where=map(lambda x:1,range(1000000))
test=[]

def im(p,q,who,vec,si):
	global where
	global test
	
	wi=vec[si]
	r=0
	i=wi+1
	while i < p and where[i]:
		i+=1
		r+=1
	i=wi-1
	l=0
	while i >= 0 and where[i]:
		i-=1
		l+=1
	#print r,l,wi,p
	#print where
	return l+r

def bf(deep,p,q,who,vec,count):
	global where
	if deep<q:
		mc = 999999999
		for i in xrange(q):
			if not who[i]:
				who[i]=deep+1
				where[vec[i]]=0
				#print deep
				m = im(p,q,who,vec,i)
				test.append(m)
				mm = bf(deep+1,p,q,who,vec,count+m)
				if mm < mc:
					mc = mm
				test.pop()
				who[i]=0
				where[vec[i]]=1
		return mc
	else:
		#print count
		##print who
		#print test
		#print '--------------'
		return count
	
def solve(p,q,vec):
	#print '-----'
	who=map(lambda x:0,range(len(vec)))
	ret=bf(0,p,q,who,vec,0)
	return ret

			
def readVector(f):
	vec=[]
	string=f.readline()
	words=string.split()
	for x in words:
		vec.append(int(x))
	return vec
	
def readVectorDec(f):
	vec=[]
	string=f.readline()
	words=string.split()
	for x in words:
		vec.append(int(x)-1)
	return vec
	
def main():
	if len(sys.argv)!=3:
		raise Exception('You should pass names of input and output files')	
	f=open(sys.argv[1])
	r=open(sys.argv[2],'w')
	t=int(f.readline())
	for i in xrange(t):
		v=readVector(f)
		p=v[0]
		q=v[1]
		vec=readVectorDec(f)
		res=solve(p,q,vec)
		r.write('Case #%d: %d\n' % (i+1, res))
	f.close()
	r.close()
	
main()
