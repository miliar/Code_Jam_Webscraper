import math

t = int(input())

def insertsorted(n,val):
	if len(n)==0:
		n = [val]
		return n
	if val > n[-1]:
		n = n + [val]
		return n
	for i in range(len(n)):
		if val<=n[i]:
			n[i:i] = val, # What the
			return n

def stall(n,k):
	b = [n]
	maxindex = 0
	v1,v2 = 0,0
	for i in range(k): ## Add k people to the stalls
		maxval = b.pop(-1)
		v1,v2 = (maxval//2-1 if maxval%2==0 else maxval//2), maxval//2
		b = insertsorted(b,v1)
		b = insertsorted(b,v2)

	return sorted([v1, v2], reverse=True)

def stall2(n,k):
	logk = math.log2(k)
	l = math.floor(logk)
	b = [n]
	for i in range(l):
		nb = []
		for j in b:
			nb.append(j//2-1 if j%2==0 else j//2)
			nb.append(j//2)
		b = nb
	b.sort(reverse=True)
	r = b[k-2**l]
	return sorted([r//2-1 if r%2==0 else r//2, r//2], reverse=True)


for i in range(t):
	n,k = [int(x) for x in input().split(" ")]
	ma, mi = stall2(n, k)
	print("Case #{}: {} {}".format(i+1, ma, mi))