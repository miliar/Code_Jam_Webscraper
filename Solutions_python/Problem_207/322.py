#debug 
def pr(*a):
	#return
	for x in a: print x,
	print

def nextPos(n, i):
	i += 2
	if i in (n, n+1):
		i = 1
	return i
	
def run(rs,ys,bs):
	aa = [(len(rs), rs), (len(ys), ys), (len(bs),bs)]
	aa.sort(reverse=True)
	n = len(rs)+len(ys)+len(bs)
	if aa[0][0]*2 > n:
		return "IMPOSSIBLE"
	arr = [0] * N
	i = 0
	for t in aa[0][1]:
		arr[i] = t
		i = nextPos(n,i)
	for t in aa[1][1]:
		arr[i] = t
		i = nextPos(n,i)
	for t in aa[2][1]:
		arr[i] = t
		i = nextPos(n,i)
	assert arr[0] != arr[-1]
	r,y,b=0,0,0
	for t in arr:
		if t=="R": r += 1
		if t=="Y": y += 1
		if t=="B": b += 1
	assert r==len(rs)
	assert y==len(ys)
	assert b==len(bs)
	for i in range(1,len(arr)):
		assert arr[i] != arr[i-1]
	return "".join(arr)
'''
def simple(r,y,b):
	n = r+y+b
	if r*2 > n or y*2>n or b*2 > n:
		return "IMPOSSIBLE"
	arr = [0] * N
	i = 0
	for t in range(r):
		arr[i] = "R"
		i = nextPos(n,i)
	for t in range(y):
		arr[i] = "Y"
		i = nextPos(n,i)
	for t in range(b):
		arr[i] = "B"
		i = nextPos(n,i)
	return "".join(arr)'''

def solve(n, r,o,y,g,b,v):
	if o+g+v==0:
		return run(["R"]*r, ["Y"]*y,["B"]*b)
	else:
		if b<o or y < v or r < g:
			return "IMPOSSIBLE"
		if r*2 > n or y*2>n or b*2 > n:
			return "IMPOSSIBLE"
		b2 = b-o
		y2 = y-v
		r2 = r-g
		m = max(b2,y2,r2)
		
		pass
	pass
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	line = f.readline().strip()
	pr(line)
	N, R,O,Y,G,B,V = [ int(x) for x in line.split()]
	rt = solve(N,R,O,Y,G,B,V)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()