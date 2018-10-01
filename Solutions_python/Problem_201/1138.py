from math import log, floor

def level_min(n, l):
	for i in range(l):
		n = n / 2 -1 if n%2 == 0 else (n-1)/2
	return n

def build_table(n, l):
	table = [(1,0)]
	for i in range(l):
		x = level_min(n, i)
		if x == 0:
			num_x = 0
			num_xp = 2 * table[i] + table[i][0]
		elif x % 2 == 0:
			num_x = table[i][0]
			num_xp = 2 * table[i][1] + table[i][0]
		else:
			num_x = 2 * table[i][0] + table[i][1]
			num_xp = table[i][1]
		table.append((num_x, num_xp))	
	return table

def compute_range(n, level, tp):
	lm = level_min(n, level)
	length = lm
	if tp == "minp":
		length = lm +1
	if length % 2 == 0:
		return length/2 - 1, length/2
	else:
		return (length-1)/2, (length-1)/2
	
def solve(n, k):
	level = int(floor(log(k, 2)))
	table = build_table(n, level)
	k_rem = k - pow(2, level) + 1
	min_num = table[level][0]
	minp_num = table[level][1]
	#print level
	#print table
	if k_rem <= minp_num:
		ans = compute_range(n, level, "minp")
	else:
		ans = compute_range(n, level, "min")
		
	return ans

if __name__=='__main__':
	t = int(raw_input())
	for i in range(t):
		n, k = raw_input().split(" ")
		n = int(n)
		k = int(k)
		l, r  = solve(n, k)
		print "Case #%d: %d %d" % (i+1, r, l)
