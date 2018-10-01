mul = {}
mul[(0,1)] = 1
mul[(0,2)] = 2
mul[(0,3)] = 3
mul[(0,4)] = 4
mul[(1,1)] = 1
mul[(1,2)] = 2
mul[(1,3)] = 3
mul[(1,4)] = 4
mul[(2,1)] = 2
mul[(2,2)] = -1
mul[(2,3)] = 4
mul[(2,4)] = -3
mul[(3,1)] = 3
mul[(3,2)] = -4
mul[(3,3)] = -1
mul[(3,4)] = 2
mul[(4,1)] = 4
mul[(4,2)] = 3
mul[(4,3)] = -2
mul[(4,4)] = -1

def formatIP(ip):
	res = []
	for ele in ip:
		char = 2 if ele == 'i' else 3 if ele == 'j' else 4
		res.append(char)

	return res

def isNotPossible(x):
	ele = x[0]

	for i in xrange(1, len(x)):
		if x[i] != ele:
			return False

	return True

def makeHash(formattedIP):
	h = {}

	l = len(formattedIP)
	res = formattedIP[l-1]

	h[l-1] = res

	i = l-2
	while i >= 0:
		res = mul[(formattedIP[i], res)] if res >= 0 else -mul[(formattedIP[i], -res)]
		h[i] = res 

		i -= 1

	return h

def getSolution(ip):
	global mul

	formattedIP = formatIP(ip)

	l = len(formattedIP)

	if isNotPossible(formattedIP):
		return 'NO'

	hashed = makeHash(formattedIP)
#	print formattedIP
	r1 = 0
	for i in xrange(l-2):
		r1 = mul[(r1, formattedIP[i])] if r1 >= 0 else -mul[(-r1, formattedIP[i])]
		if r1 == 2:
			if i+1 >= l:
				break

			r2 = 0
			for j in xrange(i+1, l-1):
				r2 = mul[(r2, formattedIP[j])] if r2 >= 0 else -mul[(-r2, formattedIP[j])]
				if r2 == 3:
					if j+1 >= l:
						break

					r3 = hashed[j+1]
					#for k in xrange(j+1, l):
					#	r3 = mul[(r3, formattedIP[k])] if r3 >= 0 else -mul[(-r3, formattedIP[k])]

					if r3 == 4:
						return 'YES'
	return 'NO'


T = int(raw_input())

for i in xrange(1, T+1):
	(L, X) = map(int, raw_input().split())
	ip = raw_input()
	fullip = ip * X

	print 'Case #' + str(i) + ': ' + str(getSolution(fullip))