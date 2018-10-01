import os
import math


input=open("input.txt","r")
r=input.readline()

n=r
n=int(n)+1
print n

r=input.readline()
K=1

R=open("output.txt","w")
R.close()

while K < n:
	L=[]
	j=0
	A=""
	for i in range(0,len(r)-1):
		if r[i]<>" ":
			A=A+r[i]
		if r[i] ==" ":
			A=int(A)
			L.append(A)
			A=""
			j=j+1
	A=int(A)
	L.append(A)
	
	print L
	nbgoogler = L[0]
	nbsurprise = L[1]
	note = L[2]
	L.remove(int(nbgoogler))
	L.remove(int(nbsurprise))
	L.remove(int(note))
	L.sort()
	print L
	L_best_score=[]
	nbsurprise=int(nbsurprise)
	for s in L:
		print s
		if nbgoogler!=0:
			nbgoogler=nbgoogler-1
			if (math.floor((s/3))+2)<note :
				L_best_score.append(0)
			if (math.floor((s/3)+2))>=note :
				if nbsurprise == 0:
					if s%3 == 2 :
						L_best_score.append(((s+1)/3))
					if s%3 == 1 :
						L_best_score.append(((s+2)/3))
					if s%3 == 0 :
						L_best_score.append((s/3))
				if nbsurprise != 0:
					nbsurprise=nbsurprise-1
					if s%3 == 2 :
						if (((s+1)/3)+1)>=note:
							L_best_score.append(((s+1)/3)+1)
						if (((s+1)/3)+1)<note:
							L_best_score.append(((s+1)/3))
							nbsurprise=nbsurprise+1
					if s%3 == 1 :
						L_best_score.append((s+2)/3)
						nbsurprise=nbsurprise+1
					if s%3 == 0 :
						if s==0:
							L_best_score.append(0)
							nbsurprise=nbsurprise+1
						if s!=0:
							if ((s/3))>=note:
								L_best_score.append((s/3))
								nbsurprise=nbsurprise+1
							if ((s/3))<note :
								if ((s/3)+1)<note:
									L_best_score.append(0)
									nbsurprise=nbsurprise+1
								if ((s/3)+1)>=note:
									L_best_score.append((s/3)+1)
		print L_best_score					
	print L_best_score
	
	N=0
	
	for h in L_best_score:
		if h>=note:
			N=N+1
	
	R=open("output.txt","a")
	R.write("Case #")
	R.write(str(K))
	R.write(": " + str(N) + "\n")
	R.close()
	K = K+1
	r=input.readline()
	print "next step"
	
    
R.close()
