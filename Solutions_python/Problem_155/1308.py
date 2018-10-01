import sys
sys.stdin=open('1.in', 'r')
sys.stdout=open('1.out','w')
for t in range(input()):
	n,s=raw_input().split()
	cnt=int(s[0])
	ans=0
	for i in range(1,len(s)):
		if i>cnt: 
			ans+=i-cnt
			cnt=i
		cnt+=int(s[i])
	print 'Case #%d:'% (t+1), ans