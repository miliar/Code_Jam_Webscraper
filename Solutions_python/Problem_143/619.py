f=open('B-small-attempt0.in','r')
o=open('obs','w+')
t=int(f.readline())
ti=1
while ti<=t :
	abk=f.readline().strip().split()
	a,b,k=[int(v) for v in abk]
	la=[v for v in range(a)]
	lb=[v for v in range(b)]
	s=0
	# if ti==1:
	# 	print la
	# 	print lb
	# 	print k
	# else:
	# 	break

	for va in la:
		for vb in lb:
			if va&vb < k:
				s+=1

	ss= str("Case #")+str(ti)+str(": ")+ str(s)+str("\n")
	o.write(ss)
	# print s
	ti+=1
