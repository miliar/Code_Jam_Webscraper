import sys

fi = open('one.in', 'r')
T = int(fi.readline().rstrip('\n'))

for i in range(1,T+1):
		value = fi.readline().strip().split('/')
		P = int(value[0])
		Q = int(value[1])

		if Q == 1:
				print 'Case #%d: %d' % (i,0)
				continue
		elif P != 1 and (Q % P) == 0:
				Q = Q / P
				P = 1

		if (Q & (Q - 1)) != 0:
				print 'Case #%d: %s' % (i,'impossible')
		else:
				result = 0
				while P < Q and (Q & 1) == 0:
						Q >>= 1
						result += 1
				if P < Q:
						print 'Case #%d: %s' % (i,'impossible')
				else:
						print 'Case #%d: %d' % (i,result)

