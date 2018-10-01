import re

raw_lines = open("q1input.txt").readlines()
lines = raw_lines[1:]
output = open("q1output.txt", "w")
for case, line in enumerate(lines, start=1):
	s_max = int(re.search("(^[0-9]+)", line).group(0))
	quantities = [int(q) for q in re.search("([0-9]+)$", line).group(0)]
	friends = 0
	applauding = quantities[0]
	# Starting from quantities[1], make sure that there are enough people currently
	# applauding to make everyone in the current index applaud. Continue.
	for required, quantity in enumerate(quantities[1:], start=1):
		if required > applauding:
			friends += (required-applauding)
		applauding = sum(quantities[:required+1]) + friends
	print("Case #{}: {}".format(str(case), str(friends)), file=output)