import sys

name = "A-small-attempt5"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())
for testCase in range(1, testCases + 1):
	answer1 = input()
	data1=[]
	for i in xrange(4):
		line=raw_input()
		for u in line.split():
			data1.append(int(u))
	list1=data1[(answer1-1)*4:(answer1-1)*4+4:1]
	answer2=input()
	data2=[]
	for i in xrange(4):
		line=raw_input()
		for u in line.split():
			data2.append(int(u))
	list2=data2[(answer2-1)*4:(answer2-1)*4+4:1]
	ans=[x for x in list1 if x in list2]
	if(len(ans)==1):
		print("Case #" + str(testCase) + ": " + ("%d" % ans[0]))
	elif (len(ans)>1):
		print("Case #" + str(testCase) + ": Bad magician!")
	else:
		print("Case #" + str(testCase) + ": Volunteer cheated!")