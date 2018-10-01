import fileinput
import math

########################################################
# functions
########################################################
def solve(jono):
	jo=[]
	for t in jono:
		jo.append(int(t))
	if len(jo)<2:
		return 0
	pituus=len(jo)
	lisa=0
	while 1:
		ok=1
		for p in range(1,pituus):
			if sum(jo[:p])<p:
				ok=0
		if ok==1:
			break
		lisa=lisa+1
		jo[0]=jo[0]+1
	return lisa
	
				
########################################################
# main
########################################################
f = fileinput.input("A-large.in")
T = int(f.readline())
i = 0
for line in f:
	i=i+1
	row = line.split()
	m = int(row[0])
	p = str(row[1])	
	answer=solve(p)
	print "Case #%i: %i"%(i,answer)
	
	

