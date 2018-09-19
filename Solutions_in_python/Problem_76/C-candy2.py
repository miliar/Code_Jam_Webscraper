def binary(candy):
	result = []
	for i in range(len(candy)):
		ans = ""
		x = candy[i]
		while x > 0:
			a = x % 2
			ans = str(a) + ans
			x = int(x/2)
		result.append(ans)
	return result

def decimal(binary):
	result = 0
	for i in range(len(binary)):
		result = result*2
		result = result + int(binary[i])
	return result

def PatSum(bag):
	if bag == []:
		return "0"
	result = bag[0]
	for i in range(1,len(bag)):
		x = bag[i]
		y = result
		if len(x) > len(y):
			while len(x) > len(y):
				y = '0' + y
		elif len(y) > len(x):
			while len(y) > len(x):
				x = '0' + x
		temp = ""
		for j in range(len(y)):
			if x[j] == y[j]:
				temp = temp + '0'
			else:
				temp = temp + '1'
		result = temp
	return decimal(result)				

fi = open('C-large.in','r')
fo = open('C-large.out','w')

T = int(fi.readline().strip())
for t_no in range(T):
	N = int(fi.readline().strip())
	C = [int(x) for x in fi.readline().split(' ')]
	C.sort()
	bC = binary(C)
	for i in range(1,len(C)):
		bag1 = bC[:i]
		bag2 = bC[i:]
		x = PatSum(bag1)
		y = PatSum(bag2)
		if x == y:
			r = sum(C[:i])
			s = sum(C[i:])
			if r >= s:
				result = r
			else:
				result = s
			break
		else:
			result = "NO"
	print result
	fo.write("Case #%d: %s\n" % (t_no + 1, str(result)))
	
fi.close()
fo.close()