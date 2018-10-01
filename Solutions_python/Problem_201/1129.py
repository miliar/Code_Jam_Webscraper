def find_space(space_dict):
	k = space_dict.keys()
	k.sort()
	max_space = k[-1]
	space_dict[max_space] -= 1
	if space_dict[max_space] == 0:
		space_dict.pop(max_space)

	remain_space = max_space - 1
	l_space = remain_space / 2
	r_space = remain_space / 2
	if remain_space % 2 == 1:
		r_space += 1

	if l_space > 0:
		if l_space not in space_dict:
			space_dict[l_space] = 1
		else:
			space_dict[l_space] += 1

	if r_space > 0:
		if r_space not in space_dict:
			space_dict[r_space] = 1
		else:
			space_dict[r_space] += 1

	return l_space, r_space


T = int(raw_input())

for i in xrange(T):
	N, K = [int(s) for s in raw_input().split(" ")]

	space_dict = {}
	space_dict[N] = 1

	for person in xrange(K):
		l_space, r_space = find_space(space_dict)

		if person == K - 1:
			print "Case #%d: %d %d" % (i + 1, max(l_space, r_space), min(l_space, r_space))
