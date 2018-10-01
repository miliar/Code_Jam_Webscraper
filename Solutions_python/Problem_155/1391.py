n=int(input())
for t in range(n):
	s = [int(c) for c in input().split()[1]]
	print("Case #%d:"%(t+1),max([0]+[i-sum(s[:i]) for i in range(len(s))]))
