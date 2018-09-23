import heapq
import sys
def foo(n,k):
	l=[-n]
	for i in xrange(k):
		x=-heapq.heappop(l)
		heapq.heappush(l,-((x-1)/2))
		heapq.heappush(l,-((x-1)/2+(x-1)%2))
	return (x-1)/2+(x-1)%2,(x-1)/2

inputfile = open(sys.argv[1])
lines = inputfile.readlines()

testcase=0
for line in lines[1:]:
	testcase+=1
	n,k = int(line.split()[0]) , int(line.split()[1])
	x,y=foo(n,k)
	print "Case #%d: %d %d"%(testcase,x,y)
