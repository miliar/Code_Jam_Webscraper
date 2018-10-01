f = open('score.txt','r')
qq = open('output.txt','w')
totalcase = int(f.readline())
for i in range(totalcase):
	n,s = map(str,f.readline().split())
	#print "wwww",s[0],s[1],s[2],s[3],s[4]
	c=0;
	ans=0
	for j in range(len(s)):
		#print s[j]
		if c>=j :
			c+=int(s[j])
		elif s[j]!='0' :
			#print "This is",j,c,j-c
			ans+=j-c
			c+=j-c+int(s[j])
	qq.write("Case #"+str(i+1)+": "+str(ans)+"\n")
