
def abss(x):
	if x < 0:
		return -x
	else:
		return x

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a%b)


C = int(raw_input())

for tp in range(C):
	tc = raw_input().split()
	n = int(tc[0])
	V = [0] * n
	for i in range(n):
		V[i] = int(tc[i+1])
	T = abss(V[1]-V[0])
	for i in range(n):
		for j in range(i):
			T = gcd(T, abss(V[i]-V[j]))

	print "Case #" +str(tp+1) +  ":", (T - (V[0]%T))%T%T






