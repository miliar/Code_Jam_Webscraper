def solve_fair(naomi, ken):
	used_ken = [False for _ in ken]
	count = 0
	for n in reversed(naomi):
		found = False
		for ind, k in enumerate(ken):
			if k > n and not used_ken[ind]:
				found = True
				used_ken[ind] = True
				break
		if not found:
			for ind, k in enumerate(ken):
				if not used_ken[ind]:
					used_ken[ind] = True
					break
			count += 1
	return count

def solve_unfair(naomi, ken):
	spent = 0
	c_naomi = len(naomi) - 1
	c_ken = len(ken) - 1
	while c_naomi >= spent:
		if naomi[c_naomi] > ken[c_ken]:
			c_naomi -= 1
			c_ken -= 1
		else:
			spent += 1
			c_ken -= 1
		pass
	return len(naomi) - spent

ncases = int(raw_input());
for i in xrange(ncases):
	number = int(raw_input())
	naomi = sorted([float(a) for a in raw_input().split()])
	ken = sorted([float(a) for a in raw_input().split()])
	print "Case #{}: {} {}".format(i+1, solve_unfair(naomi, ken), solve_fair(naomi, ken))