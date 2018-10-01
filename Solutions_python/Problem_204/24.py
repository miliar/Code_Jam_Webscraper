import math

def try_match(row): #returns boolean success
	m, mm = math.floor(min(row)), math.ceil(max(row))
	while m <= mm:
		c = math.floor((m+mm)/2)
		can = 0
		for k in row:
			if c*0.9 > k:
				can = 1
				break
			if c*1.1 < k:
				can = 2
				break
		if can is 0:
			return True
		elif can is 1:
			mm = c-1
		elif can is 2:
			m = c+1
	return False


def solve(n, p, r, q):
	row = []
	for i in range(n):
		q[i] = sorted([ k/float(r[i]) for k in q[i] ])
		row.append(q[i][-1])

	ans = 0
	while True:
		if try_match(row):
			ans += 1
			for i in range(n):
				q[i].pop()
				if len(q[i]) == 0:
					return ans
				row[i] = q[i][-1]
		else:
			ind = row.index(max(row))
			q[ind].pop()
			if len(q[ind]) == 0:
				return ans
			row[ind] = q[ind][-1]
	return ans



t = int(raw_input())

for testNum in range(t):
	n, p = map(int, raw_input().split())
	r = map(int, raw_input().split())
	q = [map(int, raw_input().split()) for i in range(n)]

	print "Case #{}: {}".format(testNum+1, solve(n, p, r, q))