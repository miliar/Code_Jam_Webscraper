fin = open("A-large.in","r")
fout = open("A-large.out","w")
fread = fin.readline
#fread = input

from operator import itemgetter
from math import pi

def foo(base,k,a):
	baseR,baseH,a[base][0],a[base][1] = a[base][0],a[base][1],0,0

	va = [[2*pi*i[0]*i[1],i[0]] for i in a]
	va.sort(reverse=True)

	mxR = baseR
	ans = 2*pi*baseR*baseH
	for i in range(k-1):
		ans+=va[i][0]
		mxR = max(mxR,va[i][1])

	ans+=pi*mxR**2
	a[base][0],a[base][1] = baseR,baseH

	return ans

def main(tcase):
	n,k = [int(inpNum) for inpNum in fread().strip().split()]
	a = [[int(inpNum) for inpNum in fread().strip().split()] for i in range(n)]

	ans = 0
	for i in range(n):
		ans = max(ans,foo(i,k,a))
	print("Case #%d: %.10f"%(tcase,ans), file = fout)

for tcase in range(int(fread().strip())):
	main(tcase+1)
fout.close()
fin.close()