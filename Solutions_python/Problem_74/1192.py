"""M=int(raw_input())
P=float(raw_input())
X=int(raw_input())

def millionaire(round_num,probab,probab1,now,now1):
	if round_num<=M:
		if now<=X:
			print "<",probab+probab1*P,now
			return millionaire(round_num+1,probab+probab1*P,probab1*(1-P),now+now1/2,now1/2)
		else:
			print ">",probab,now
			return millionaire(round_num+1,probab,probab1*(1-P),now-now1/2,now1/2)
	else:
		return probab
		
	
print millionaire(0,0,1,500000,500000)"""
import sys

I=int(sys.stdin.readline())
for i in range(I):
	count=0
	B=1
	O=1
	Bl=[]
	Ol=[]
	Bp=0
	Op=0
	T=map(str,sys.stdin.readline().split(" "))
	T[-1]=T[-1][:-1]
	for j in range(1,len(T),2):
		if T[j]=="B":
			Bl.append(T[j+1])
		else:
			Ol.append(T[j+1])
	for j in range(2,len(T),2):
		flago=0
		flagb=0
		while T[j]!=0:
			if B==int(T[j]) and T[j-1]=="B":
				T[j]=0
				Bl.pop(0)
				flagb=1
			elif O==int(T[j]) and T[j-1]=="O":
				T[j]=0
				Ol.pop(0)
				flago=1
			if flagb==0 and len(Bl)!=0:	
				if B<int(Bl[0]):
					B+=1
				elif B>int(Bl[0]):
					B-=1
			if flago==0 and len(Ol)!=0:
				if O<int(Ol[0]):
					O+=1
				elif O>int(Ol[0]):
					O-=1
			count+=1
	sys.stdout.write("Case #")
	sys.stdout.write(str(i+1)+": ")
	sys.stdout.write(str(count)+"\n")
"""	for j in range(1,len(T),2):
		if T[j]=="O":
			Ol+=T[j+1]
		elif T[j]=="B":
			Bl+=T[j+1]
			
	print Bl,Ol
	while Bl!=[] or Ol!=[]:
		
		if len(Bl)!=0:
			q=int(Bl[0])
			print Bl,Ol
			if B==q and (Op-Bp==1):
				Bl.pop(0)
				Bp+=1
			elif B<q:
				B+=1
			elif B>q:
				B-=1
		
		if len(Ol)!=0:
			w=int(Ol[0])
			if O==w and (Op-Bp==0):
				Ol.pop(0)
				Op+=1
			elif O<w:
				O+=1
			elif O>w:
				O-=1
			count+=1
		print Bl,Ol"""
	#print "Case #%d:"%i+1,
	#print count