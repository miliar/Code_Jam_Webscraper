# your code goes here
import sys

lines = sys.stdin.readlines()

stripped = []

for line in lines:
	stripped.append(line.strip("\n"))
	
count = int(stripped[0])

content = stripped[1:]
casenum=1
for x in content:
	shymax = int(x.split(" ")[0])
	datastr = x.split(" ")[1]
	total = int(datastr[0])
	invites = 0
	if shymax == 0:
		outstr = "Case #"+str(casenum)+": "+str(invites)
		print outstr
		casenum+=1
		continue
	for i,j in enumerate(datastr[1:]):
		if i+1 > total:
			while i+1 > total:
				total+=1
				invites+=1
			
		
		total+= int(j)
	outstr = "Case #"+str(casenum)+": "+str(invites)
	print outstr
	casenum+=1
	
	
