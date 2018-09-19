def solve(c,o,invoke): 
	print c
	print o
	print invoke
	
	if invoke.count==0:
		return []
	print 'start'
	c1=[]
	c2=[]
	for s in c:
		c1.append(s[0:2])
		c2.append(s[2])
	
	a=[]
	for i in invoke:
		if a==[]:
			a.append(i)
			continue
		#combs:
		comb=0
		for j in range(len(c1)):
			if c1[j]==a[-1]+i or c1[j]==i+a[-1]:
				a[-1]=c2[j]
				comb=1
				break
		if comb==0:
			a.append(i)
		#opp:
		for s in o:
			if s[0] in a and s[1] in a:
				a=[]
				break
		
	return a

#main
from time import time
if __name__ == "__main__":
	def getInts():
		return map(int, input.readline().rstrip('\n').split(' '))
	start_time=time()
	output = open('c:/gcj/output', 'w')
	input = open("c:/gcj/in.txt", "r")
	T = int(input.readline())
	for case in range(1, T + 1):
		line=input.readline().rstrip('\n').split(' ')
		
		c=int(line.pop(0))
		combs = line[:c]
		del line[:c]
		
		d=int(line.pop(0))
		oppos = line[:d]
		del line[:d]
		
		n=int(line[0])
		invoke=line[1]
		
		ans = solve(combs,oppos,invoke)
		ans = '[' + ", ".join(ans) + ']'
		s = "Case #%d: %s\n"%(case, ans)
		print s,
		output.write(s)
	print "Total time: %d msec"%(1000*(time()-start_time))