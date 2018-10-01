from sys import stdin, stdout
def test(t):
	h = []
	while t > 0:
		h.append(t%10)
		t/=10
	l = len(h)
	for i in range(l/2):
		if h[i] != h[l-1-i]:
			return False
	return True
def constuct(n, o):
	res = 0
	p = 1
	m = n
	while m > 0:
		res = res*10+m%10
		m /= 10
		p*=10
	if o == 1:
		p /= 10
	return n*p+(res%p)
tot = 0
pos = []
def dfs(j,left,mul,add,o):
	if j == 0:
		global tot,pos
		t = constuct(add, o)
		tot+=1
		pos.append(t*t)
		#print t*t
	else:
		dfs(j-1,left,mul/10,add,o)
		if left > 0:
			dfs(j-1,left-1,mul/10,add+mul,o)


i = 1
j = 0
tot = 0
pos=[1,4,9,121,484]
while i < 10**24:
	dfs(j,3,i,i*10,1)
	dfs(j,3,i,i*10+1,1)
	dfs(j,1,i,i*10+2,1)
	dfs(j+1,3,i,i*10,0)
	dfs(j,0,i,i*20+1,1)
	dfs(j,0,i,i*20,0)
	dfs(j,0,i,i*20,1)
	i *= 10
	j += 1
pos.sort()
instream = open('C-large-2.in','r')
outstream = open('C-large-2.txt', 'w')
R = lambda:map(int,instream.readline().split())
ca = int(instream.readline())
for c in range(ca):
	A,B = R()
	add = 0
	for i in pos:
		if i >= A and i <= B:
			add+=1
		if i > B:
			break
	outstream.write('Case #%d: %d\n'%(c+1,add))