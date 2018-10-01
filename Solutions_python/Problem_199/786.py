# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def ask1(n,m):
	#print(n)
	cnt=0
	for i in range(0,len(n)):
		#print(n)
		if n[i]=="-" and i>len(n)-m:
			return "IMPOSSIBLE"
		elif n[i]=="-":
			cnt+=1
			for j in range(i,i+m):
				n[j] = '+' if n[j]=='-' else '-'
	return cnt

	
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [str(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  #print(list(n)," ",m)
  print "Case #{}: {}".format(i, ask1(list(n),int(m)))
  # check out .format's specification for more formatting options