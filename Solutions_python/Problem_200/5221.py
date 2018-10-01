def isTidy(num):
	strNum = str(num)
	for i in range(0,len(strNum)-1):
		if (strNum[i] > strNum[i+1]):
			return False
	return True	
# read number of test cases
t = int(input())  
for tt in range(1, t+1):
	# read number of input per test case
	N = int(input())
	# read the test data for test case, note test data is int 
	while(not isTidy(N)):	
		N = N - 1;
		#print(N)
	print("Case #" + str(tt) + ": "+str(N))
