import code
from operator import itemgetter
from itertools import starmap
input=open("in.txt","r")
output=open("out.txt","w")
n_cases=int(input.readline())
for case in range(1,n_cases+1):
	n=int(input.readline())
	points=[]
	for i in range(n):
		points.append(tuple(map(int, input.readline().split())))
	points.sort()
	points=enumerate(points)
	points=list(starmap(lambda i, p: (p[1],i), points))
	points.sort()
	positions=list(map(itemgetter(1), points))
	cnt=0
	
	for i in range(n):
		if positions[i]==i:
			continue
		#Position it
		loc=positions.index(i)
		cnt+=abs(loc-i)
		no_loc=positions[:loc]+positions[loc+1:]
		positions=list(range(i+1))+no_loc[i:]
	output.write("Case #{0}: {1}\n".format(case,cnt))

		
		
		