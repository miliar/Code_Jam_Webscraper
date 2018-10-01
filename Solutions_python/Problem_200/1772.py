import sys
import bisect

inputfile = open(sys.argv[1])
lines = inputfile.readlines()
testcases = int(lines[0].split()[0])

l=[i for i in xrange(1,100) if i%10>=i/10 or i<10]
def mysearch(x):
	if x==0:
		return "09"
	res = l[bisect.bisect(l,x)-1]
	if res<10:
		return "0"+str(res)
	else:
		return str(res)
testcase=0
for line in lines[1:]:
	testcase+=1
	x=int(line.split()[0])
	#print x,
	if x<100:
		print("Case #%d: %d"%(testcase,int(mysearch(x))))
	else:
		nums=list(str(x))
		for  i in xrange(len(nums)-1,0,-1):
			a,b=list(mysearch(int(nums[i-1]+nums[i])))
			nums[i-1]=a
			nums[i]=b
			if (int(nums[i])==9):
				for j in xrange(i,len(nums)):
					nums[j]='9'
		res=int("".join(nums))
		print("Case #%d: %d"%(testcase,res))

