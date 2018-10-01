class train:
    trainA=[];
    trainB=[];
    nA=0
    nB=0;
            
            
    def readinput(self):
        import string
##        print 'hi'
        file=open("B-large.in",'r')#B-small-attempt0.inB-small-attempt1.in
        p=file.readline()
	#print p
        ans=open("small.out",'w')
        count1=int(p)
        k1=0
	#print 'gffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
        while(k1<count1):
            self.trainA=[];
            self.trainB=[];
	    self.nA=0;
	    self.nB=0;
	    
            
            k1=k1+1
	    p=file.readline()
	    p.strip(' ')
	    #print 'p is', p
            turnA=int(p)
	    p=file.readline()
	    f=p.split(' ')
	    self.nA=int(f[0])
	    self.nB=int(f[1])
	    
	    i=0;
	    while i<self.nA:
		    p=file.readline()
		    f=p.split(' ')
		    #print 'f ',f
		    hs=f[0].split(':')
		    #print 'hs ',hs
		    ka=int(hs[0])*60+int(hs[1])
		    hs=f[1].split(':')
		    kb=int(hs[0])*60+int(hs[1])
		    k=[ka,kb]
		    #print k
		    self.trainA.append(k)
		    i=i+1
            i=0
	    while i<self.nB:
		    p=file.readline()
		    f=p.split(' ')
		    
		    hs=f[0].split(':')
		    kb=int(hs[0])*60+int(hs[1])
		    hs=f[1].split(':')
		    ka=int(hs[0])*60+int(hs[1])
		    
		    k=[kb,ka]
		    #print k
		    self.trainB.append(k)
		    i=i+1
		    
            noA=self.nA
	    noB=self.nB
	    temp=[]
	    tempa=[]
	    for l in self.trainB:
		    temp.append(l[1])
	    for l in self.trainA:
		    tempa.append(l[0])
            
	    tempa.sort()
            temp.sort()
	    tempi=0
	    nAA=0
	  
	    for j in tempa:
		    #if tempi<len(temp):
		         #print 'j ',j,'  temp[tempi]',temp[tempi] 
		    if tempi<len(temp) and int(j)>=(int(temp[tempi])+turnA):
			    tempi=tempi+1
		    else:
			    nAA=nAA+1			    		    		   
				   
	    
		
			   
            
            temp=[]
	    tempa=[]
	    for l in self.trainA:
		    temp.append(l[1])
            for l in self.trainB:
		    tempa.append(l[0])    
	    
            tempa.sort()
            temp.sort()
	    tempi=0
	    nBB=0
	    
	    for j in tempa:
		    #if tempi<len(temp):
		    	#print 'j ',j,'  temp[tempi]',temp[tempi] 
		    if tempi<len(temp) and int(j)>=(turnA+int(temp[tempi])):
                            tempi=tempi+1

		    else:
			    nBB=nBB+1	
	  
            	    
	    
		
			    
			    
		     
            ans.write("Case #"+str(k1)+": "+str(nAA)+" "+str(nBB)+"\n")
	    count=0
            
   
if __name__=="__main__":
    m=train()
    m.readinput()
