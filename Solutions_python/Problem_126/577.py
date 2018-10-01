import sys


def substring(string):
	j=1
	a=[]
	while True:
		for i in range(len(string)-j+1):
		    a.append(string[i:i+j])
		if j==len(string):
		    break
		j+=1
		#string=string[1:]
	return a
	
def check(L,n):
	count=0
	x=['a','e','i','o','u']
	for l in L:
		if len(l)>=n:
			l=l.replace('e','a')
			l=l.replace('i','a')
			l=l.replace('o','a')
			l=l.replace('u','a')
			A=l.split('a')
			for a in A:
				if len(a)>=n:
					count=count+1
					break
	return count
	
def main():
	sys.stdin=open("input.in","r")
	sys.stdout=open("output.out","w+")
	T=int(input())
	for t in range(T):
		L=input().split(' ')
		N=int(L[1])
		count=check(substring(L[0]),N)
		print('Case #{0}: {1}'.format(t+1,count))
	sys.stdin=sys.__stdin__
	sys.stdout=sys.__stdout__
	
main()