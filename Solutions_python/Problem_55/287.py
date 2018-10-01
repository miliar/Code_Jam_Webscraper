'''
Codejam template

@author: alarobric
'''

from collections import deque

def solve():
	r, k, n = [int(z) for z in infile.readline().split()]
	queue = deque([int(z) for z in infile.readline().split()])
	print "R, K, N", r, k, n
	print queue
	
	total = 0
	
	for i in range(r):
		riders = 0
		groups = 0
		while(1):
			#print queue
			if queue[0] <= k-riders and groups <n:
				rider = queue.popleft()
				queue.append(rider)
				riders += rider
				groups += 1
			else:
				break
		#print riders, "total riders"
		total += riders
	return total

filepath = '/home/alan/Downloads/'
fileprefix = 'C-small-attempt0' #Change me!

infilename = filepath + fileprefix + '.in'
outfilename = filepath + fileprefix + '.out'
infile = open(infilename, 'rU')
outfile = open(outfilename, 'w+')

numCases = int(infile.readline())
print numCases

for case in range(1, numCases+1):
	str = "Case #%d: %d" %(case, solve())
	print str
	outfile.write(str + "\n")

infile.close()
outfile.close()
