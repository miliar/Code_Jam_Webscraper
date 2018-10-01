import sys

inp = sys.stdin.readline().strip().split()
N = int(inp[0])

for n in xrange(N):
	L = list(str(sys.stdin.readline().strip()))
	L = ['0'] + L
	i = len(L) - 1
	while L[i] == '0': i -= 1
	cnts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	while i > 0:
		#print "#", L, ",", i, j, ",", cnts
		if L[i - 1] == '0':
			cnts[int(L[i])] += 1
			i -= 1
			special = (i == 0)
			L.pop(i)
			k = i
			while k < len(L) and L[k] == '0': k += 1
			L.insert(k + 1, '0')
			#print "##", L
			while i < len(L):
				#print "##", L, ",", i, ",", cnts
				if L[i] != '0':
					k = 1
					while cnts[k] == 0: k += 1
					L[i] = str(k)
					cnts[k] -= 1
				i += 1
			if special:
				Z = list(L)
				while L[-1] == '0':
					L.pop(-1)
					L.insert(1, '0')
					if Z == L: break
			break
		elif L[i - 1] < L[i]:
			#print "##", L, ",", i, ",", cnts
			cnts[int(L[i])] += 1
			cnts[int(L[i - 1])] += 1
			k = int(L[i - 1]) + 1
			while cnts[k] == 0: k += 1
			L[i - 1] = str(k)
			W = list()
			while L[-1] == '0':
				L.pop(-1)
				W.append('0')
			L = L[:i] + W + L[i:]
			cnts[k] -= 1
			while i < len(L):
				#print "##", L, ",", i, ",", cnts
				if L[i] != '0':
					k = 1
					while cnts[k] == 0: k += 1
					L[i] = str(k)
					cnts[k] -= 1
				i += 1
			break
		else: # L[j] >= L[i]:
			cnts[int(L[i])] += 1
			i -= 1
	if L[0] == '0': L.pop(0)
	print "Case #%d: %s" % (n + 1, "".join(L))

