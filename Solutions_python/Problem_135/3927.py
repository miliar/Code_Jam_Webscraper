f1 = open("C:\Practice\Python\output2",'w')
with open("C:\Practice\Python\A-small-attempt1.in") as f:
	t=int(f.readline())
	for k in xrange(t):
	    fi=int(f.readline())
	    fa=[]
	    for _ in xrange(4):
	        fa.append([int(x) for x in f.readline().split()])
	    s=int(f.readline())
	    sa=[]
	    for _ in xrange(4):
	        sa.append([int(x) for x in f.readline().split()])
	    c=0
	    fs,ss,n,id=sorted(fa[fi-1]),sorted(sa[s-1]),0,False
	    #print fs,ss
	    for i in fs:
	    	for j in ss:
	    		if i==j:
	    			n=i
	    			c+=1
	    		if c>1:
	    			id=True
	    			break
	    	if id:
	    		break
	    if c==0:
	        f1.write("Case #"+str(k+1)+": Volunteer cheated!")
	        f1.write("\n")
	    elif c==1:
	        f1.write("Case #"+str(k+1)+": "+str(n))
	        f1.write("\n")
	    else:
	        f1.write("Case #"+str(k+1)+": Bad magician!")
	        f1.write("\n")
	    
