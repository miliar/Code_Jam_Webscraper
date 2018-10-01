#!/usr/bin/python
import sys
import math

def isPal(num):
	if num <=0:
		return False
	if num <10:
		return True

	snum = str(num)
	snum2 = snum[::-1]
	if snum == snum2 :
		return True
	return False

def getall(tmin, tmax):
	n=tmin
	resn = []
	ress = []
	n = int(math.pow(tmin, 0.49))
	while True:
		#print "Test ", n
		if isPal(n):
			ps = n*n
			if isPal(ps) and ps <=tmax:
				resn.append(n)
				ress.append(ps)
			if ps > tmax:
				break
		n += 1
	return [resn, ress]

ta = int(math.pow(10, 14)+1)
_resalln = getall(1, ta)
allns = _resalln[0]
allres = _resalln[1]

def treatcase(line, j):
	#print "Case #%d: %s"%(j, line)
	arr = line.split()
	if len(arr)!= 2:
		print "ERROR"
		return 
	start = int(arr[0])
	end = int(arr[1])
	if start > end :
		print "ERROR"
		return 

	n = start
	res = 0
	for n in allres:
		if n >= start and n <=end:
			res += 1
		n += 1
	print "Case #%d: %d"%(j, res)
	
def testmain():
	if(len(sys.argv)<2):
		return

	fname = sys.argv[1]
	f = open(fname)
	line=f.readline()
	Ts = int(line.strip())
	
	#print Ts
	j=0
	N=0
	M=0

	part = []
	n = 0
	while True:
		j += 1
		if(j>Ts):
			return
		line=f.readline()
		line = line.strip()
		if len(line) <=0:
			break
		treatcase(line, j)

	
if __name__ == "__main__":
	testmain()
	#res = getall(1, 1000)
	#print res
