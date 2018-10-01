import math

def closest_palin(a):
	A = [c for c in str(a)]
	l = len(A)
	odd = l%2
	A_ = [c for c in ((A[l/2+odd:])[::-1])]
	B = A[:l/2]
	if A_ < B:
		return (A[:l/2 + odd]+(A[:l/2])[::-1])
	elif A_ == B:
		return A
	else:
		full = True
		for i in range(l/2 + odd -1,-1,-1):
			if A[i] < '9':
				A[i] = str(int(A[i])+1)
				full = False
				break
			else:
				A[i] = '0'
		if full:
			A = A.insert(0,'1')
			l = l+1
			odd = 1- odd
			return (A[:l/2 + odd]+(A[:l/2])[::-1])
		else:
			return (A[:l/2 + odd]+(A[:l/2])[::-1])
			
def check_palin(a):
	A = str(a)
	l = len(A)
	odd = l%2
	return (A[:l/2] == (A[l/2+odd:])[::-1])
	

def palin_check(a,b):
	#print a,b,
	A = closest_palin(a)
	l = len(A)
	odd = (l % 2)
	A_ = (A[l/2+odd:])
	A = A[:(l/2 + odd)]
	l = l/2 + odd
	sum = 0
	a = int(''.join(A+A_))
	if(a<=b):
		if check_palin(a*a):
				#print a
				sum = sum+1
	while(a<=b):
		full = True
		for i in range(l-1,-1,-1):
			if(A[i] < '9'):
				A[i] = str(int(A[i])+1)
				if not(i == l-1 and odd == 1):
					A_[l-1-odd-i] = A[i]
				full = False
				break
			else:
				A[i] = '0'
				if not(i == l-1 and odd == 1):
					A_[l-1-odd-i] = '0'
		if 	full:
			if odd == 1:
				A[0] = '1'
				A_.append('1')
			else:
				A.insert(0,'1')
				A_[l-odd-1] = '1'
			l = l+1-odd
			odd = 1 - odd
		#print A,' ',A_
		a = int(''.join(A+A_))
		if(a <= b):
			if check_palin(a*a):
				#print a
				sum = sum+1
	return sum			

t = input()
for i in range(t):
	a,b = map(int,raw_input().split())
	print 'Case #'+str(i+1)+': '+str(palin_check(int(math.ceil(math.sqrt(a))),int(math.floor(math.sqrt(b)))))
	