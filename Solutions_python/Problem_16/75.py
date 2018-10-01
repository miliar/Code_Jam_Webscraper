def xpermutations(items):
    return xcombinations(items, len(items))


def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc


def find_min(l, k):
	p = xpermutations(range(1, k+1))
	return min([comp(l, perm) for perm in p])

def comp(l, p):
	cp = l[:]
	for i in range(0, len(l), len(p)):
		
		for j, letter in enumerate(p):

			cp[i+j] = l[i+letter-1]
	letter = None
	count = 0
	for a in cp:
		if a != letter:
			count += 1
			letter = a
	return count

def main():
	num = input()
	for i in range(1, num+1):
		k = input()
		l = list(raw_input())
		m = find_min(l, k)
		print "Case #%d: %d" % (i, m)

main()
