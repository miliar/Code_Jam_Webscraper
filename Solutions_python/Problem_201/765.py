def exe3(n,m):
	slot=1
	space=n
	res=[]
	while(m>0):
		if m<=slot:
			temp = space-space/(slot)*slot
			if temp>0 and temp>=m: #lost div
				space=space/(slot)
			else:
				space=space/(slot)-1
			if space/2*2!=space:	
				res.append(space/2+1)
			res.append(space/2)
			return res
		else:
			m=m-slot
			space =space-slot
			slot = slot*2


import time
start = time.time()
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n, m = [str(s) for s in raw_input().split(" ")]
	res = exe3(int(n),int(m))
	print "Case #{}: {} {}".format(i,max(res),min(res))
  # check out .format's specification for more formatting options
end = time.time()
#print(end - start)
