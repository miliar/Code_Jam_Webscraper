import math
def is_square(n):
    return math.sqrt(n).is_integer()
f = open("input.in","r")
out = open("output.txt","w")
arr = f.readlines()
cases = int(arr[0][:-1])
arr.pop(0)
for i in xrange(0,cases-1):
	arr[i] = arr[i][:-1]
for i in xrange(0,cases):
	cred = arr[i].split(" ")
	minm = int(cred[0])
	maxm = int(cred[1])
	count = 0
	filtered = []
	for j in xrange(minm, maxm+1):
		if is_square(j):
			filtered.append(j)
	for j in filtered:
		if str(j) == str(j)[::-1]:
			if str(int(math.sqrt(j))) == str(int(math.sqrt(j)))[::-1]:
				count +=1 						
	out.write("Case #"+str(i+1)+": "+str(count)+"\n")