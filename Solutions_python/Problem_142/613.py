T = int(raw_input())
for case in xrange(T):
	N = int(raw_input())
	error = False
	strings = []
	for n in xrange(N):
		strings.append(list(raw_input()))
	value_sets = []
	for n in xrange(N):
		value_sets.append([])
		value_sets[n] = [strings[n][0]]
		for value in strings[n]:
			if value is not value_sets[n][-1]:
				value_sets[n].append(value)
	for n in xrange(1,N):
		if len(value_sets[n]) != len(value_sets[0]):
			error = True
			break
		for i in xrange(len(value_sets[n])):
			if value_sets[n][i] is not value_sets[0][i]:
				error = True
				break
		if error:
			break

	sizes = []
	for n in xrange(N):
		index = 0
		sizes.append([])
		for key, value in enumerate(value_sets[0]):
			sizes[n].append(0)
			while index < len(strings[n]) and strings[n][index] == value:
				index += 1
				sizes[n][key] += 1
			if sizes[n][key] == 0:
				error = True
				break
		if error:
			break

	cost = 0
	if error:
		cost = "Fegla Won"
	else:
		for key in xrange(len(value_sets[0])):
			min_cnt = 100
			max_cnt = 0
			for n in xrange(N):
				if min_cnt > sizes[n][key]:
					min_cnt = sizes[n][key]
				if max_cnt < sizes[n][key]:
					max_cnt = sizes[n][key]
			cost += max_cnt - min_cnt

	print "Case #" + str(case+1) + ":",cost
