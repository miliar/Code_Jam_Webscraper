import string
def flip(s, k, x):
	if (x + k) <= len(s):
		for i in range(x, k+x):
			if s[i] == "-":
				s[i] = "+"
			else:
				s[i] = "-"
	else:
		return "IMPOSSIBLE"
	#print ("{}\{}\{}".format(s,k,x))
	return s
def solve(s, k):
	ans=0
	#print (s)
	for i in range(0, len(s)):
		if s[i] == "-":
			s=flip(s, k, i)
			if s == "IMPOSSIBLE":
				return s
			ans+=1
	return ans

t=int(input())
for cas in range(1,t+1):
	row = input()
	row = row.split(" ")
	s = list(row[0])
	k = int(row[1])
	print ("Case #{}: {}".format(cas,solve(s, k)))