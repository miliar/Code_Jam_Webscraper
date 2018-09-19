from math import sqrt

def consvow(s,limit):
	count = 0
	maxc = 0
	for c in s:
		if c not in 'aeiou':
			count += 1
			if count > maxc: maxc = count
			if maxc >= limit:
				break
			# print c, '->', count, maxc
		else:
			count = 0
	return maxc

def solve():

	str, n = [z for z in raw_input().split()]
	n = int(n)

	count = 0

	# print "--------------"
	for start in range(0,len(str)):
		for end in range(start+1,len(str)+1):
			s = str[start:end]
			nv = consvow(s,n)
			if nv >= n:
				count += len(str)-end+1
				break
			# print s, count

	# print count

	return count

# main()

numcases = int(raw_input())

for casenum in range(1, numcases+1):
    res = solve()
    print "Case #%d: %d" % (casenum, res)

