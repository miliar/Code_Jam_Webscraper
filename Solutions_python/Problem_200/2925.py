for t in range(int(raw_input())):
	ans=''
	y=raw_input()
	if int(y[0]*len(y))>int(y):
		if y[0]=='1':
			ans='9'*(len(y)-1)
		else:
			ans=str(int(y[0])-1)+'9'*(len(y)-1)
	elif int(y[0]*len(y))==int(y):
		ans=y
	else:
		for i in range(1,len(y)):
			if int(y[i])<int(y[i-1]):
				i=i-1
				if int(y[i]*len(y))>int(y[i:]):
					if y[i]=='1':
						ans='9'*(len(y[i:])-1)
					else:
						ans=str(int(y[i])-1)+'9'*(len(y[i:])-1)
				break
		if i==len(y)-1:
			ans=y
		else:
			ans=y[:i]+ans
	print "Case #%d: %s" %(t+1,ans)
