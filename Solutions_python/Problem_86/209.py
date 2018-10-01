input = open("C-small-attempt0.in").read().split("\n")

def check(a, v):
	return all([a[i]%v==0 or v%a[i]==0 for i in xrange(len(a))])

def check2(a, L,H):
	if L<=1<=H:	return 1
	for i in xrange(L, H+1):
		if check(a,i):
			return i
	return False

T = int(input[0])
output = []
line=1
for t in xrange(1,T+1):
	N, L, H = [int(x) for x in input[line].split()]	
	line+=1
	a = [int(x) for x in input[line].split()]
	line+=1
	a = [x for x in a if x>1]
	r = check2(a, L, H)
	r = "NO" if not r else r
	output.append("Case #"+str(t)+": "+str(r))
	
	
#print output
open("c.out","w").write("\n".join(output))