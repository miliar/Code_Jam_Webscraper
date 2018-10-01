def flipme(i,k):
	global s
	if i+k>len(s): return 0
	s = s[0:i]+s[i:i+k].replace('+','/').replace('-','+').replace('/','-')+s[i+k:]
	return 1

for t in range(int(input())):
	[s,k] = [i for i in input().strip().split(' ')]
	k = int(k)
	flip = 0
	for i in range(len(s)):
		if s[i]=="+": 
			# print("Continuing for i=",i)
			continue
		r = flipme(i,k)
		if r:
			# print("Flip success for",i)
			flip+=1
		else:
			# print("Flip fail for",i)
			print("Case #{0}: IMPOSSIBLE".format(t+1))
			break
	else:
		print("Case #{0}: {1}".format(t+1,flip))