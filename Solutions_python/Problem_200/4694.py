t = int(input())

def m(t):
	temp = str(t)
	c = len(temp)
	while(list(temp) != sorted(list(temp))):
		temp = str(temp)
		tempLen = len(temp)
		temp = int(temp)
		temp -= 1
		temp = abs(temp)
		temp = str(temp)
	print(int(temp))

for j in range(t):
	n = int(input())
	print("Case #"+str(j+1)+": ",end = '')
	m(n)	 