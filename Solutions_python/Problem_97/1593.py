with open("input") as fp:
	fp.readline()
	
	out_file = open("output", "w")
	for current_line, line in enumerate(fp.readlines()):
		start, end = line.split()

		permutations = []
		for current in range(int(start), int(end) + 1):
			current_ = str(current)
			for limit in range(len(current_)):
				tmp = current_[limit:] + current_[0:limit]
				new_item = (min(int(tmp), current), max(int(tmp), current))
				if current_ != tmp and int(start) <= int(tmp) <= int(end) and new_item not in permutations:
					permutations.append(new_item)

		out_file.write("Case #%s: %s\n" % (current_line + 1, len(permutations)))

	out_file.close()

