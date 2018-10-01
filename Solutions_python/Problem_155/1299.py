def testcase(inp):
	maxs=int(inp[0])
	inp=map(int,inp[1])
	count=0
	temp=0
	for i in range(len(inp)):
		if(temp+count<i and inp[i]>0):
			count+=i-temp-count
		temp+=inp[i]
	return count
testcases=int(raw_input())
out=open("outputA","w")
for i in range(testcases):
	temp=raw_input().split(" ")
	temp[1]=list(temp[1])
	temp=testcase(temp)
	out.write("Case #"+str(i+1)+": "+str(temp)+"\n")
out.close()
