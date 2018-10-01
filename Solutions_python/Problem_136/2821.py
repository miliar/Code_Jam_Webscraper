def test(C,F,X,acce):
	time = 0
	k = X/acce
	m = C/acce+X/(acce+F)
	while k > m:
		time += C/acce
		acce += F
		k = X/acce
		m = C/acce+X/(acce+F)
	return time + X/acce

case = int(raw_input())
cases = []
C = []
F = []
X = []
for i in range(case):
	row = raw_input().split()
	C.append(float(row[0]))
	F.append(float(row[1]))
	X.append(float(row[2]))
for k in range(len(C)):
	acce = 2
	m = test(C[k],F[k],X[k],acce)
	cases.append("Case #%d: %f" % (k+1,m))

for l in cases:
	print l

