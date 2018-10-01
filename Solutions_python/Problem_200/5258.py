def tidy(n):
	li = list()
	while n > 0:
		li.append(n%10)
		n = n // 10
	li.reverse()
	flag = False
	truecount = 0
	falsecount = 0
	if(len(li) == 1):
		return True
	for i in range(len(li)-1):
		if(li[i+1] - li[i]) >= 0:
			truecount += 1
		else:
			falsecount += 1
	if(falsecount == 0):
		return True
	else:
		return False


t = int(input())
count = 1
while t:
	test = 1
	n = int(input())
	while n:
		if tidy(n):
			print("Case "+"#"+str(count)+":"+" "+str(n))
			break
		n -= 1
	count += 1
	test += 1
	t -= 1