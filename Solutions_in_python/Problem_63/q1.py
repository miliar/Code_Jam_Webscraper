import code
from operator import itemgetter
from itertools import starmap
input=open("in.txt","r")
output=open("out.txt","w")
n_cases=int(input.readline())
for case in range(1,n_cases+1):
	L,P,C=map(int,input.readline().split())
	i=0
	while True:
		n=2**i
		fact=C**n
		if L*fact>=P:
			break
		i+=1
	output.write("Case #{0}: {1}\n".format(case,i))