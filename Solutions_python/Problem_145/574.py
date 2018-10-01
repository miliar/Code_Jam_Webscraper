from fractions import gcd

def power2(n):
	k, m = 0, 0
	while n:
		if n & 1 != 0:
			k += 1
		m += 1
		n >>= 1
	return (k, m)

T = int(input())
for i in range(1, T+1):
	p, q = map(int, input().split('/'))
	d = gcd(p, q)
	p, q = p // d, q // d
	k, m = power2(q)
	print('Case #%d:' % i, k == 1 and (m - power2(p)[1]) or 'impossible')
