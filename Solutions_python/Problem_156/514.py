from math import floor, ceil, sqrt
import bisect

with open("2.in") as f:
	lines_in = [l.strip() for l in f]

ncases = int(lines_in[0])

for i in range(1, ncases+1):
	n_diners = int(lines_in[2*i - 1])
	p = [int(x) for x in lines_in[2*i].split()]
	p.sort()

	
#	print(str(p) + " + 0")
	
	X = sum(p)
	
	# let N be the number of nonempty plates at the beginning
	# basically we're trying to find partitions a_i that solve
	# min{ max_i a_i + count(a_i > 0) - N }
	# such that sum(a_i) = sum(p_i)
	#
	# this reduces to finding a number of partitions K where K solves
	# min (sum(p) / K + K - N)
	#
	# which is given by:
	part_size = sqrt(X)
	
	# consider all sizes that give same "cost"
	sizes_to_consider = [int(floor(part_size)), int(ceil(part_size))]
	offset = 1;
	good = True
	while good:
		good = False
		Ksmall = int(floor(part_size))
		Klarge = int(ceil(part_size))
		if X/(Klarge + offset) + Klarge + offset == X/Klarge+Klarge:
			sizes_to_consider.append(Klarge + offset)
			good = True
			
		if offset < Ksmall and X/(Ksmall - offset) + Ksmall - offset == X/Ksmall+Ksmall:
			sizes_to_consider.append(Ksmall - offset)
			good = True
		
		offset += 1
		
		
	# discrete though, so consider both floor(.) and ceil(.)
	p_orig = [x for x in p] # copy
	min_cost_total = ()
	for compare_to_p in [False, True]:
		for part in sizes_to_consider:
			p = [x for x in p_orig]
#			print('---- part = ' + str(part) + ' ----')
			costs = [p[-1]] # cost after each iteration. e.g. costs[0] = max(p)
			switches = 0
			# split until all plates have no more than part_size pancakes
			done = p[-1] <= part + 1
			while not done:
				tosplit = p.pop()
			
				if p and compare_to_p:
					thispart = min( min(p), part )
				else:
					thispart = part
		
				part_a = int(round(thispart))
				part_b = tosplit - part_a
		
				bisect.insort(p, part_a)
				bisect.insort(p, part_b)
		
				switches += 1
				costs.append(p[-1] + switches)
		
#				print(str(p) + " + " + str(switches))
		
				done = p[-1] <= part + 1

			min_cost_total = min(min_cost_total, min( costs ))

	print("Case #{0}: {1}".format(i,min_cost_total))
#	raw_input("PRESS ENTER TO CONTINUE")
