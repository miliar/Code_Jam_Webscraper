def genmasks(a, b):
	start = ~(~0 << b) << (a - b)
	return (start >> i for i in range(0,a - b + 1))

for t in range(1, int(input()) + 1):
	datai, sizei = tuple(input().replace("+","1").replace("-","0").split())
	data, size, length = int(datai,2), int(sizei), len(datai)
	l = genmasks(length, size)
	changes = []
	for i, e in enumerate(l):
		temp = data ^ e
		#print("length:{} ,i:{}, res:{}".format(length,i,length-i-1))
		if (1 << length - i - 1) & temp:
			data = temp
			changes.append(e)
	#print(["{0:b}".format(i) for i in changes])
	#print(data, "{0:b}".format(data),~(~0 << length))
	if data == ~(~0 << length):
		result = len(changes)
	else:
		result = "IMPOSSIBLE"
	print("Case #{}:".format(t), result)