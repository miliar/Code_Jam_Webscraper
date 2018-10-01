#anilkumarravuru
def getSort(n):
	s = str(n)
	flag = 0
	for i in range(len(s)-1):
		if s[i]>s[i+1]:
			flag = 1
			return getSort( ((n/10**(len(s)-i-1))*10**(len(s)-i-1)) - 1 )
	if flag == 0:
		return n
T = int(raw_input())
for t in range(T):
	n = int(raw_input())
	print("Case #{}: {}".format(t+1, getSort(n)))

