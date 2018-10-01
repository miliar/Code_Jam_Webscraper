import math
f=open('C-small-attempt0.in','r+')
T=int(f.readline())

#Create a list of all palindroms between 1 to 1000
L=[float(x) for x in range(1,10)]
L+=[float(x+x*10) for x in range(1,10)]
L+=[float(x+y*10+x*100) for x in range(1,10) for y in range(10)]
#Get the min and max
for i in range(1,T+1):
	minmax=f.readline()
	A,B = map(int, minmax.split(' '))
	try:
		L.index(A)
		Aindex=L.index(A)
	except:
		L.append(A)
		L.sort()
		Aindex=L.index(A)
		L.remove(A)
	try:
		L.index(B)
		Bindex=L.index(B)
	except:
		L.append(B)
		L.sort()
		Bindex=L.index(B)-1
		L.remove(B)
	LRoot=map(lambda x: math.sqrt(x), L[Aindex:Bindex+1])
	answer=set(LRoot) & set(L)
	stri = "Case #" + str(i) + ": "
	stri += str(len(answer))
	print stri
