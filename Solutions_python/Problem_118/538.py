import decimal
dec = ['1','2','3']
for i in range(49):
	dec.append('1'+'0'*i+'1')
	dec.append('2'+'0'*i+'2')
for i in range(24):
	dec.append('1'+'0'*i+'1'+'0'*i+'1')
	dec.append('1'+'0'*i+'2'+'0'*i+'1')
	dec.append('2'+'0'*i+'1'+'0'*i+'2')
for i in range(24):
	for mid in range(47-2*i):
		dec.append('1'+'0'*i+'1'+'0'*mid+'1'+'0'*i+'1')
for i1 in range(23):
	for i2 in range(23-i1):
		dec.append('1'+'0'*i1+'1'+'0'*i2+'1'+'0'*i2+'1'+'0'*i1+'1')
		dec.append('1'+'0'*i1+'1'+'0'*i2+'2'+'0'*i2+'1'+'0'*i1+'1')
for i1 in range(23):
	for i2 in range(23-i1):
		for mid in range(45-i1*2-i2*2):
			dec.append('1'+'0'*i1+'1'+'0'*i2+'1'+'0'*mid+'1'+'0'*i2+'1'+'0'*i1+'1')
for i1 in range(22):
	for i2 in range(22-i1):
		for i3 in range(22-i1-i2):
			dec.append('1'+'0'*i1+'1'+'0'*i2+'1'+'0'*i3+'1'+'0'*i3+'1'+'0'*i2+'1'+'0'*i1+'1')
for i1 in range(22):
	for i2 in range(22-i1):
		for i3 in range(22-i1-i2):
			for mid in range(43-i1*2-i2*2-i3*2):
				dec.append('1'+'0'*i1+'1'+'0'*i2+'1'+'0'*i3+'1'+'0'*mid+'1'+'0'*i3+'1'+'0'*i2+'1'+'0'*i1+'1')
for i1 in range(21):
	for i2 in range(21-i1):
		for i3 in range(21-i1-i2):
			for i4 in range(21-i1-i2-i3):
				dec.append('1'+'0'*i1+'1'+'0'*i2+'1'+'0'*i3+'1'+'0'*i4+'1'+'0'*i4+'1'+'0'*i3+'1'+'0'*i2+'1'+'0'*i1+'1')

num = [decimal.Decimal(i)*decimal.Decimal(i) for i in dec]
num.sort()
num.append(decimal.Decimal('10')**decimal.Decimal(100))

T = int(input())
for case in range(T):
	A, B = (int(i) for i in input().split())
	print("Case #{:d}: ".format(case+1), end='')
	indexa = 0
	while num[indexa]<A:
		indexa += 1
	indexb = 0
	while num[indexb]<=B:
		indexb += 1
	print(indexb-indexa)