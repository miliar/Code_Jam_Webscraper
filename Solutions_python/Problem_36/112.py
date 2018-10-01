# -*- coding: utf-8 -*-

tcases=int(raw_input())

ref='welcome to code jam'

for tcase in range(1,tcases+1):
	line=raw_input()
	#print line
	dp=([[]]*(len(ref)+1));
	for i in range(len(dp)):
		dp[i]=([0]*(len(line)+1))
	for i in range(len(line)):
		dp[len(ref)][i]=1
	
	for p in range(len(line)-1,-1,-1):
		for i in range(len(ref)-1,-1,-1):
			#print p,i
			dp[i][p]=dp[i][p+1]
			#print line[p],ref[i],line[p]==ref[i]
			if(line[p]==ref[i]):
				dp[i][p]+=dp[i+1][p]
				dp[i][p]%=10000
		#print
	
	#for i in range(len(ref)):
	#	print ref[i],dp[i]
	
		
	print 'Case #%d: %.4d'%(tcase,dp[0][0])
	#break