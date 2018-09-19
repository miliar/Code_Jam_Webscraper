#fi=open("A-small-attempt1.in",'r')#Input File
fi=open("A-large.in",'r')#Input File
#fi=open("A.in",'r')#Input File
#fo=open("A-small-attempt.out","w")#Output File
fo=open("A-large.out","w")#Output File


T=int(fi.readline())
for case in range(1,T+1,1):
	n= fi.readline().split()
	cnt = last = 0

	pb = po = 1 
	lb = lo = 0
	for i in range(1,int(n[0])*2+1,2):
		if n[i]=="B" and abs(int(n[i+1])-pb)>cnt-lb :
			  cnt=abs(int(n[i+1])-pb)+lb+1
			  #print(n[i]+" "+str(n[i+1])+" "+str(cnt))
			  lb=cnt
			  pb=int(n[i+1])
		elif n[i]=="O" and abs(int(n[i+1])-po)>cnt-lo :
			  cnt=abs(int(n[i+1])-po)+lo+1
			  #print(n[i]+" "+str(n[i+1])+" "+str(cnt))
			  lo=cnt
			  po=int(n[i+1])
		elif n[i]=="B":
			cnt=cnt+1
			#print(n[i]+" "+str(n[i+1])+" "+str(cnt))
			lb=cnt
			pb=int(n[i+1])
		elif n[i]=="O":
			cnt=cnt+1
			#print(n[i]+" "+str(n[i+1])+" "+str(cnt))
			lo=cnt
			po=int(n[i+1])
	#print cnt
	fo.write("Case #"+str(case)+": "+str(cnt)+"\n")
