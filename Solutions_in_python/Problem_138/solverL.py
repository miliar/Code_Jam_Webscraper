
inp = open ('inputL.txt', 'r')

cases = int(inp.readline())

for i in range(cases):
	size=int(inp.readline())
	naomi = [float(j) for j in inp.readline().split()]
	ken =[float(j) for j in inp.readline().split()]
	naomi.sort()
	ken.sort()
	N = naomi
	K = ken
	fair = 0
	fN = N[:]
	fK = K[:]
	for k in range(size):
		if fN[-1]>fK[-1]:
			fair +=1
			fN.pop(-1)
			fK.pop(0)
		else:
			fN.pop(-1)
			fK.pop(-1)
	unfair = 0
	for k in range(size):
		if N[0]>K[0]:
			unfair += 1
			N.pop(0)
			K.pop(0)
		elif N[0]<K[0]:
			N.pop(0)
			K.pop(-1)
		elif N[-1]>K[-1]:
			unfair += 1
			N.pop(-1)
			K.pop(0)
		else:
			N.pop(0)
			K.pop(-1)
	print("Case #", i+1, ': ', unfair, ' ', fair, sep='')
	
