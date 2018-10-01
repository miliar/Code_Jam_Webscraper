import copy
import math

T = int(raw_input().strip())


for i in range(T):
	N = int(raw_input().strip())
	inter=0
	m=[]
	for j in range(N):
		At,Bt = (raw_input().strip()).split(' ')
		A = int(At)
		B = int(Bt)
		for p in m:
			if ((A > p[0]) and (B < p[1])) or ((A < p[0]) and (B > p[1])):
				inter = inter+1
		m.append([A,B])
	s = 'Case #' + repr(i+1) + ': ' + repr(inter)
	print s
