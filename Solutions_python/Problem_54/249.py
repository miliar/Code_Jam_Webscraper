import sys;

def nwd(a,b):
	if b==0:
		return a
	else:
		return nwd(b,a%b);


ci = -1;

for line in sys.stdin:
	t = line.split()
	ci = ci+1;
	if ci==0:
		continue
	t = t[1:]
	t = map(int, t)
	w = min(t)
	b = [p-w for p in t]
	k = 0;
	for x in b:
		k = nwd(k,x);
	print "Case #" + str(ci) + ": " + str((k-w%k)%k);
