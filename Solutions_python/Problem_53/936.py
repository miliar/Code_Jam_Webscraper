##hello .. this is my first time at code jam.. 
#started learning python 2 days before... :) so thigs arent solid 
#i am not sure how i should be parsing the input file... 
#any way this reads from 'A-small.in' from the same directory
#thank u
from numpy import *
def lastOn(n):
	for i in range(1,n):
		if arr[i]==1:
			continue
		else:
			arr[i]=1
			return(i)

def cascadeOff(y):
	arr[1:y]=0
	
def lightOn(n):
	for i in range(1,n):
		if i==n-1 and arr[i]==1:
			return(1)
		if arr[i]==1:
			continue
		else:
			return(0)
			

f = open('A-small-attempt1.in', 'r')
d = open('1', 'w')
data=int(f.readline())
l=0

for line in f:
	if l==data+1:
		break
	else:
		l+=1
	str=line.split(' ')
	n=int(str[0])
	k=int(str[1])
	arr=zeros(n+1,int)
	arr[0]=1
	for x in range(1,k+1):
		y=lastOn(n+1)
		cascadeOff(y)
	if lightOn(n+1):
		d.write('Case #{0}: ON\n'.format(l))
	else:
		d.write('Case #{0}: OFF\n'.format(l))









