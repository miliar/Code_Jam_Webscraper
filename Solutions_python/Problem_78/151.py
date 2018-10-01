import sys

def abs(x):
	if x>=0: return x
	else: return -x

def min(x,y):
	if x<y: return x
	else: return y

def max(x,y):
	if x>y: return x
	else: return y

def gcd(x,y):
	while x!=y:
		t=min(x,y)
		s=max(x,y)
		if t==0: return s
		x=t
		y=s-t
	return x

def pos(n,d,g):
	den=100/gcd(100,d)
	if d!=g and (g==100 or g==0): return False
	if n<den: return False
	return True

case=int(raw_input())
for repeat in xrange(case):
	line=raw_input().split()
	n=int(line[0])
	d=int(line[1])
	g=int(line[2])
	sys.stdout.write("Case #%d: " %(repeat+1))
	if pos(n,d,g): print "Possible"
	else: print "Broken"