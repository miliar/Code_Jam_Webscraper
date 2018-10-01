def exe1(list1,sp):
	ctr=0
	for i in xrange(0,len(list1)-sp+1):
		if list1[i]=='-':
			ctr+=1
			for j in range(0,sp):
				if list1[i+j]=='-':
					list1[i+j]='+'
				else:
					list1[i+j]='-'
	for k in xrange(len(list1)-sp+1,len(list1)):
		if list1[k]=='-':
			return "IMPOSSIBLE"
	return ctr; 


import time
start = time.time()
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [str(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  print "Case #{}: {}".format(i, exe1(list(n),int(m)))
  # check out .format's specification for more formatting options
end = time.time()
#print(end - start)
