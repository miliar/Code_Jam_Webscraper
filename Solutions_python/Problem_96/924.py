import sys

f = sys.stdin

t = int(f.readline())

def max(num):
	p = num / 3
	if num % 3 > 0:
		p = p + 1

	return p

def unusmax(num):
	if num == 0:
		return 0

	return max(num + 2)


for i in range(1, t+1):
	print 'Case #{}:'.format(i),
	inp = map(int, f.readline().rstrip().split(' '))
	(n, s, p) = tuple(inp[:3])
	l = inp[3:]
	l.sort(reverse = True)
	cnt = 0
	for j in l:
		if max(j) >= p:
#			print 't:{}, m:{}, u:0'.format(j, max(j))
			cnt = cnt + 1
			continue

		if unusmax(j) < p or s == 0:
			break

#		print 't:{}, m:{}, u:1'.format(j, unusmax(j))
		
		s = s - 1
		cnt = cnt + 1

	print cnt
