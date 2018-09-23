#author : ash-ishh..

def ifequal(lis):
	return all(x == lis[0] for x in lis)

def flip(lis,start,end):
	for i in range(start,end+1):
		if lis[i] == "+":
			lis[i] = "-"
		else:
			lis[i] = "+"
	

T = int(input())
for i in range(T):
	s = list(input())
	k = int(input())
	count = 0
	for elem in range(len(s)-(k-1)):
		if(s[elem] == "-"):
			flip(s,elem,elem+(k-1))
			count += 1
	if(ifequal(s)):
		print("Case #{}: {}".format(i+1,count))
	else:
		print("Case #{}: IMPOSSIBLE".format(i+1))	
