def solve(n,c): 
	if n==1:
		return 'NO'
	ans=c[0]
	for i in range(1,n):
		ans=ans^c[i]
	if (ans!=0):
		return 'NO'
	m=min(c)
	s=sum(c)-m
	return s

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
		n=int(input.readline())
		c=getInts()
		ans = solve(n,c)
		s = "Case #%d: %s\n"%(case, ans)
		print s,
		output.write(s)
	print "Total time: %d msec"%(1000*(time()-start_time))