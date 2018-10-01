for t in xrange(int(raw_input())):
	n = list(raw_input())
	l = len(n)
	'''i = m	
	while i>0:
		flag = True
		s = list(str(i))
		for j in xrange(len(s)-1):
			if int(s[j])>int(s[j+1]):
				flag = False
				break
		if flag==True:
			break
		i-=1
	y.append(i)'''
	if l==1:
		print "Case #"+str(t+1)+": "+str(int(n[0]))+"\n"
	else:
		for k in xrange(100):
			i = 0
			while i<l-1:
				if int(n[i])>int(n[i+1]):
					n[i] = str(int(n[i])-1)
					for z in xrange(i+1,l):
						n[z] = '9'
					i+=1
				i+=1
			if int(n[-1])<int(n[-2]):
				n[-1]='9'
		#print int(''.join(n))
		print "Case #"+str(t+1)+": "+str(int(''.join(n)))+"\n"
