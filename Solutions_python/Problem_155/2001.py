def standing(l):
	nstanding = 0
	nadditional = 0
	for shyness, npeople in enumerate(l):
		if npeople == 0:
			continue
		elif nstanding >= shyness:
			nstanding += npeople
		else:
			nadditional += (shyness - nstanding)
			nstanding += (shyness - nstanding) + npeople
	return nadditional

if __name__ == "__main__":
	t = int(raw_input())
	for i in xrange(t):
		l = map(int, raw_input().split()[1])
		print "Case #{0}: {1}".format(i+1, standing(l))


