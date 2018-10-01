input=open("A-large.in").read().split("\n")
T=int(input[0])

def need(k):
	p = 1
	if k%4==0:
		p=4
	elif k%2==0:
		p=2
	if k%25==0:
		p*=25
	elif k%5==0:
		p*=5
	return 100/p

def possible(n, pd, pg):
	return need(pd)<=n and not (pd<pg and pg==100 or pd>pg and pg==0)

output = []
for i in xrange(1,T+1):
	n, pd, pg = [int(x) for x in input[i].split()]
	#print n, need(pd), possible(n,pd,pg), i
	if possible(n,pd,pg):
		output+= ["Case #"+str(i)+": Possible"]
	else:
		output+= ["Case #"+str(i)+": Broken"]
open("a.out", "w").write("\n".join(output))