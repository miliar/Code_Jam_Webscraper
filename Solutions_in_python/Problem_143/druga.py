n = int(input())


def test(A,B,C):
	t = {}
	s = 0
	for x in range(A):
		for y in range(B):
			if x & y < C:
				t[(x,y)] = True
			
	return len(t)


for u in range(n):
	#print ("Case ", u)
	A,B,C = map(int, input().split())
	s = 0

	A,B = max(A, B), min(A, B)

	#print (A,B,C)
	if A < C or B < C:
		a, b, _ = sorted([A, B, C])
		base = a * b
	else:
		base = C*C
	s += base
	#print ("Base ", base)
	levo = 0
	if A > C:
		levo = (A - C) * min(B, C)
	desno = 0
	if B > C:
		desno = (B - C) * min(A, C)
	#print ("Levo: ", levo, " Desno:", desno)

	s += levo + desno

	if A > C and B > C:
		for x in range(C, A):
			for y in range(C , B):
				if x & y < C:
					s+=1

	# if not test(A,B,C) == s:
	# 	print(s, test(A,B,C))
	# 	print("error", A, B, C)
	print ("Case #{}: {}".format(u+1, s))