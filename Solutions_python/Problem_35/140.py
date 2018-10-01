# -*- coding: utf-8 -*-
H=-1
W=-1
def getI(num):
    return num/W
    
def getJ(num):
    return num%W
  





if __name__=="__main__":
  global H,W
  fd=open("B-large.in","r")
  num=int(fd.readline().strip())
  print "numis ",num
  fw=open("output","w")
  for caseI in range(num):
    
    sline=fd.readline().split()
    #print sline
    H=int(sline[0])
    W=int(sline[1])
    alt=[]
    for i in range(H):
      line=fd.readline().split()
      temp=[]
      for j in line:
	temp.append(int(j))
      alt.append(temp)
    #print H,"  ",W
    #print alt
    print "alt:"
    for i in alt:
     print i
    ls=[]
    for i in range(H):
      temp=[0]*W
      ls.append(temp)
      
    #ls=[[0]*W]*H;
    for i in range(H):
      for j in range(W):
	ls[i][j]=i*W+j
	#print ls[i][j],"  ",getI(ls[i][j])," ",getJ(ls[i][j])," ",ls[getI(ls[i][j])][getJ(ls[i][j])]
    
    parent=[-1]*(H*W)
    check=[0]*(H*W)
    for i in range(H*W):
      parent[i]=i;
    sink=[]
    for k in range(H*W):
      i=getI(k)
      j=getJ(k)
      ind=[10001,10001,10001,10001]
      kI=[-1,-1,-1,-1]
      if i>0:
	ind[0]=alt[i-1][j]
	kI[0]=(i-1)*W+j;
      if j>0:
	ind[1]=alt[i][j-1]
	kI[1]=i*W+(j-1);
      if j<W-1:
	ind[2]=alt[i][j+1]
	kI[2]=i*W+(j+1);
      if i<H-1:
	ind[3]=alt[i+1][j]
	kI[3]=(i+1)*W+j;
      index=ind.index(min(ind))
      kIndex=kI[index]
      if ind[index]<alt[i][j]:
	parent[k]=parent[kIndex]
      else:
	sink.append(k)
	check[k]=1
    
    while 1:
      #print parent
      flag=0
      for k in range(H*W):
	if check[k]==1:
	  continue
	else:
	  flag=1
	  #par=parent[k]
	  child=k
	  lC=[]
	  while not child==parent[child]:
	    lC.append(child)
	    child=parent[child]
	  for c in lC:
	    parent[c]=child
	    check[c]=1
      if flag==0:
	break;
    
      
    alp=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    iA=0
    lsop=[]
    ans=[]
    for i in range(H):
      temp=[""]*W
      ans.append(temp)
    
    for k in range(len(parent)):
      #print lsop
      i=getI(k)
      j=getJ(k)
      
      if parent[k] in lsop:
	kI=lsop.index(parent[k])
	ans[i][j]=alp[kI]
      else:
	lsop.append(parent[k])
	kI=lsop.index(parent[k])
	ans[i][j]=alp[kI]

    print "ams:"
    for i in ans:
     print i
    print ""
    
    fw.write("Case #"+str(caseI+1)+":\n")
    for iD in range(H):
      str1=""
      for cD in range(W):
	str1=str1+ans[iD][cD]+" "
      str1=str1[:-1]+"\n"
      fw.write(str1)
  fw.close()
      
      

	
      
      

    #print ls
    #print parent
    
  
      

  
