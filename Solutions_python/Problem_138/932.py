import sys

T = int(sys.stdin.readline())

for case in range(1, T + 1):
	legit_wins = 0
	deceit_wins = 0
	num_blocks = int(sys.stdin.readline())
	naomi_input = [float(x) for x in sys.stdin.readline().split(' ')]
	ken_input = [float(x) for x in sys.stdin.readline().split(' ')]

	# Calculate legit wins
	naomi_blocks = [x for x in naomi_input]
	ken_blocks = [x for x in ken_input]
	for _ in range(0, num_blocks):
		naomi_best = max(naomi_blocks)
		if naomi_best > max(ken_blocks):
			ken_option = min(ken_blocks)
		else:
			ken_option = min([x for x in ken_blocks if x > naomi_best])

		if naomi_best > ken_option:
			legit_wins += 1
		naomi_blocks.remove(naomi_best)
		ken_blocks.remove(ken_option)

	# Calculate deceitful wins
	naomi_blocks = [x for x in naomi_input]
	ken_blocks = [x for x in ken_input]
	for _ in range(0, num_blocks):
		naomi_best = max(naomi_blocks)
		ken_beatable = [x for x in ken_blocks if x < naomi_best]
		if len(ken_beatable) > 0:
			ken_best = max(ken_beatable) if len(ken_beatable) > 0 else 0
			if naomi_best > ken_best:
				deceit_wins += 1
			naomi_blocks.remove(naomi_best)
			ken_blocks.remove(ken_best)	
	sys.stdout.write('Case #%d: %d %d\n' % (case, deceit_wins, legit_wins))

