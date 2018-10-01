# -*- coding: utf-8 -*-


if __name__=="__main__":
  fd=open("C-large.in","r")
  num=int(fd.readline().strip())
  print "numis ",num
  fw=open("outputlarge","w")
  for caseI in range(num):
    line=fd.readline().strip().replace(" ","#")
    serStr="welcome#to#code#jam"
    alph=[]
    matrix=[]
    for i in range(len(serStr)):
      alph.append(serStr[i])
      matrix.append(0);
    for c in line:
      tempStr="welcome#to#code#jam"
      ind=0;
      #print "for ",c
      while c in tempStr:
	index=tempStr.index(c)
	#print "["+tempStr+"]"
	#if index<len("welcome to code jam"):
	tempStr=tempStr[index+1:]
	index=index+ind
	if index==0:
	  matrix[index]=(matrix[index]+1)%10000
	else:
	  matrix[index]=(matrix[index]+matrix[index-1])%10000
	  
	#print "index is ",index,"    ind:",ind,"  "
	ind=index+1
    ans=str(matrix[-1])
    while len(ans)<4:
      ans="0"+ans
    print ans
    fw.write("Case #"+str(caseI+1)+": ")
    fw.write(ans+"\n")

      