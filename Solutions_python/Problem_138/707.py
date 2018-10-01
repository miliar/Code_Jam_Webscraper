# -- separate project  --BASE FILE for comp-----------
def readint(): return int(f.readline())
def readarray(): return [int(x) for x in f.readline().split()]

def freadarray(): return [float(x) for x in f.readline().split()]

def fun():
	N=readint()
	A=freadarray();A.sort()
	B=freadarray();B.sort()
	c1,c2=0,N;i,j=0,0
	#A tries to win
	while i<N and j<N:
		if A[i]>B[j]:
			c1+=1;i+=1;j+=1
		else: i+=1
	#B tries to loose
	i,j=0,0
	while i<N and j<N:
		if A[i]>B[j]: j+=1
		else:
			c2-=1;i+=1;j+=1


	return "%d %d"%(c1,c2)



f=open('in','r');T=readint()
for i in range(1,T+1):
    print "Case #%d: %s" %(i,fun())

