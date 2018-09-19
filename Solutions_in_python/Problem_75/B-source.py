#fi=open("B-small-attempt0.in",'r')#Input File
fi=open("B-large.in",'r')#Input File
#fi=open("B.in",'r')#Input File
#fo=open("B-small-attempt.out","w")#Output File
fo=open("B-large.out","w")#Output File


T=int(fi.readline())
for case in range(1,T+1,1):
    li = fi.readline().split()
    ip=""
    op=[]
    sa=[]
    flag=i=0
    while i < len(li):
    	if flag==0:
    		for j in range(1,int(li[i])+1):
    			sa.append([li[j+i][:2],li[j+i][2:]])
    		flag=1
    		i=i+1+int(li[0])
    	elif flag==1:
    		for j in range(1,int(li[i])+1):
    			op.append([li[i+j][0],li[i+j][1]])
    		flag=2
    		i=i+1+int(li[i])
    	else:
    		ip=li[i+1]
    		break
    ans = "["+ip[0:1]
    last = ip[0:1]
    for c in ip[1:]:
    	flag=0
    	if len(sa)>0:
		for ob in sa:
			if ob[0]==(c+last) or ob[0]==(last+c):
				ans=ans[:len(ans)-1]+ob[1]
				last = ob[1]
				flag=1
	if flag ==0 and len(op)>0:
		for ob in op:
			if (ob[0]==c and ans.find(ob[1])>=0) or  (ob[1]==c and ans.find(ob[0])>=0):
				ans = "["
				last = ""
				flag=1
				break
	if flag==0:
		if ans!="[":
			ans=ans+", "+c
		else:
			ans=ans+c
		last = c
    ans = ans+"]"
    #print ans
    
    fo.write("Case #"+str(case)+": "+ans+"\n")
