# https://code.google.com/codejam/contest/3264486/dashboard#s=p2

def bathroomStalls(n, k):
	s = [1] + [0] * n + [1]
	blank = n
	d = {n:1}
	i = l = r = 0
	while i < k:
		maxi = max(d.keys(), key=int)
		if d[maxi] >= 2:
			d[maxi] -= 1
		else:
			d.pop(maxi)
		mid = maxi / 2
		l = mid
		r = maxi - mid - 1
		if not l in d:
			d[l] = 1
		else:
			d[l] += 1
		if not r in d:
			d[r] = 1
		else:
			d[r] += 1
		i += 1
	return ' '.join([str(l), str(r)])

if __name__ == '__main__':
	t = int(raw_input())
	for i in range(1,t+1):
		n, k = map(int,raw_input().split())
		print "Case #{}:".format(i), bathroomStalls(n, k)
