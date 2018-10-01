

def naomi(blocks):
	return blocks.pop()


def naomi_deceitful(blocks, ken_blocks):
	if len(blocks) <= 1:
		block = blocks.pop()
		return block, block

	block = min(blocks)
	blocks.remove(block)
	tell = block

	# If block is smaller than any Ken's blocks get biggest block away.
	if block < min(ken_blocks):
		tell = max(ken_blocks) - 0.00000001
	# If block can win one of Ken's blocks make sure that he plays smallest.
	else:
		tell = max(ken_blocks) + 0.00000001

	return block, tell


def ken(blocks, told):
	smallest_bigger = [n for n in blocks if n > told]

	if len(smallest_bigger)	> 0:
		smallest = min(smallest_bigger)
		blocks.remove(smallest)

		return smallest

	smallest = min(blocks)
	blocks.remove(smallest)

	return smallest


in_file = open("D-large.in")
out_file = open("D-large.out", "wt")

# Skip first line
n_cases = int(in_file.readline())

case = 1

for line in in_file:
	blocks = int(line)

	NAOMI_BLOCKS = [float(n) for n in in_file.readline().split()]
	KEN_BLOCKS = [float(n) for n in in_file.readline().split()]


	naomi_blocks = list(NAOMI_BLOCKS)
	ken_blocks = list(KEN_BLOCKS)
	naomi_score_deceitful = 0

	for i in range(blocks):
		naomi_chose, told = naomi_deceitful(naomi_blocks, ken_blocks)
		ken_chose = ken(ken_blocks, told)

		if naomi_chose > ken_chose:
			naomi_score_deceitful += 1


	naomi_blocks = list(NAOMI_BLOCKS)
	ken_blocks = list(KEN_BLOCKS)
	naomi_score = 0

	for i in range(blocks):
		naomi_chose = naomi(naomi_blocks)
		ken_chose = ken(ken_blocks, naomi_chose)

		if naomi_chose > ken_chose:
			naomi_score += 1


	print("Case #%s: %s %s" % (case, naomi_score_deceitful, naomi_score))
	out_file.write("Case #%s: %s %s\n" % (case, naomi_score_deceitful, naomi_score))

	case += 1

in_file.close()
out_file.close()