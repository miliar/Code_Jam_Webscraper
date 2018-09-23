# https://code.google.com/codejam/contest/8294486/dashboard#s=p1

def stableNeigh_bors(n, r, o, y, g, b, v):
	res = [''] * n
	if r > n / 2 or o > n / 2 or y > n / 2 or g > n / 2 or b > n / 2 or v > n / 2:
		return 'IMPOSSIBLE'
	
	array = [[r, 'R'], [y,'Y'],[b,'B']]

	array = sorted(array, reverse = True)
	i = 0
	count1 = array[0][0]
	while count1 > 0:
		res[i] = array[0][1]
		i += 2
		count1 -= 1

	if n % 2 == 0:
		j = n - 1
	else:
		j = n - 2
	count2 = array[1][0]
	while count2 > 0:
		res[j] = array[1][1]
		j -= 2
		count2 -= 1

	for k in range(n):
		if res[k] == '':
			res[k] = array[2][1]

	return ''.join(res)

if __name__ == '__main__':
	t = int(raw_input())
	for i in range(1,t+1):
		n, r, o, y, g, b, v = map(int, raw_input().split())
		print "Case #{}:".format(i), stableNeigh_bors(n, r, o, y, g, b, v)
