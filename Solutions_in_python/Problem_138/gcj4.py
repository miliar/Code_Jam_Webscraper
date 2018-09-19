"""
Overview: for each farm_cost, farm_production, and goal,
keep adding farms until you no longer are getting increasing returns
"""
file = open('blocks.txt', 'r')
iters = int(file.readline())

case_count = 1

while iters > 0:
	rounds = int(file.readline())
	naomi_blocks = [float(x) for x in file.readline().split(' ')]
	ken_blocks = [float(x) for x in file.readline().split(' ')]

	# Play War.
	nb = [x for x in naomi_blocks]
	kb = [x for x in ken_blocks]
	r = rounds
	war_points = 0
	while (r > 0):
		# Naomi should burn up her largest first, but Ken will always use to minimum possible block to win, if possible.
		if max(nb) > max(kb):
			# Ken can't win, so he'll use his smallest block.
			nb.remove(max(nb))
			kb.remove(min(kb))
			war_points = war_points + 1
		else:
			# Ken will use the smallest block possible to win.
			winners = []
			for item in kb:
				if item > max(nb):
					winners.append(item)
			chosen = min(winners)
			nb.remove(max(nb))
			kb.remove(chosen)
		r = r-1

	# Play Deceitful War.
	nb = [x for x in naomi_blocks]
	nt = []
	kb = [x for x in ken_blocks]
	r = rounds
	deceitful_war_points = 0

	while (r > 0):
		if max(kb) > max(nb):
			# Naomi can't win here. Force him to burn up his biggest block.
			target = max(kb)
			subtractive = 0.00001
			must_find = True
			while must_find:
				if (target - subtractive not in ken_blocks) and (target - subtractive not in nt):
					nt.append(target)
					kb.remove(target)
					nb.remove(min(nb))
					must_find = False
				else:
					subtractive = subtractive + 0.00001
		else:
			# Use the minimum block possible to beat Ken's largest.
			winners = []
			for item in nb:
				if item > max(kb):
					winners.append(item)

			# Tell Ken whatever, fuck it.
			chosen = min(winners)
			target = max(kb)
			nt.append(chosen)
			nb.remove(chosen)
			kb.remove(target)
			deceitful_war_points = deceitful_war_points + 1

		r = r - 1

	print "Case #{num}: {naomi_deceitful_war_points} {naomi_war_points}".format(num=case_count, naomi_deceitful_war_points=deceitful_war_points, naomi_war_points=war_points)
	case_count = case_count + 1
	iters = iters - 1
