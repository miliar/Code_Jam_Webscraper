from math import pi
import sys
sys.setrecursionlimit(1000*1001)

#data = open('A-small-attempt2.in', 'r').readlines()
data = open('A-large.in', 'r').readlines()
tn = int(data[0])
answ = []
dp = 1
for t in range(tn):
	n, k = data[dp].split()
	n, k = int(n), int(k)
	a = []
	for i in range(n):
		r, h = data[dp + i + 1].split()
		r, h = int(r), int(h)
		a.append((r, 2 * pi * r * h))
	dp += 1 + n
	a.sort(reverse=True)
	#print('\n', a)
	
	mem = [[-2] * (n + 1) for i in range(n + 1)]
	# x = pos, y = taken from pos to end
	def f(x, y):
		#print(x, y)
		if y <= 0:
			r = 0
		elif x >= n:
			r = -1
		elif mem[x][y] != -2:
			return mem[x][y]
		else:
			p1, p2 = f(x + 1, y - 1), f(x + 1, y)
			if p1 != -1 and y == k:
				p1 += pi * a[x][0]**2
			if p1 == -1 and p2 == -1:
				r = -1
			elif p1 == -1:
				r = p2
			elif p2 == -1:
				r = a[x][1] + p1
			else:
				p1 += a[x][1]
				r = max(p1, p2)
		mem[x][y] = r
		return r
	
	lar = f(0, k)
	#print(mem)
	answ.append(lar)

with open('A-large.out', 'w') as f:
#with open('A-small.out', 'w') as f:
    for i, o in enumerate(answ):
        f.write('Case #{}: {:.30}\n'.format(i+1, o))
