def checkAll(check):
	number = int(check)
	for i in range(number,0,-1):
		if checkTiny(i) == True:
			break
	return i

def checkTiny(check):
	strTiny = str(check)
	listNum = []
	for digit in strTiny:
		listNum.append(int(digit))
	return all(x<=y for x,y in zip(listNum, listNum[1:]))

t = int(input())
f = open('out.txt', 'w')
for i in range(1,t+1):
	n = input()
	m = checkAll(n)
	f.write("Case #{}: {}".format(i, m) + "\n")

