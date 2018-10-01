def pancakes_flipper(k,len_s):
	all_flips = {'+'*len_s:0}
	
	to_flip = ['+'*len_s]

	level = 0 # How many flips needed to reach to the happy-faces-pancake.
	while level != None:
		# Flipping new_flippables from 'to_flip'
		new_flippables = list()
		level += 1
		for flippable in to_flip: 
			for i in range(0,len_s-k+1):
				new_flippable = ''
				for j in range(0,len_s):
					if j in range(i,i+k):
						if flippable[j] == '+':
							new_flippable +='-'
						else:
							new_flippable += '+'
					else:
						new_flippable += flippable[j]

				if new_flippable not in all_flips:
					all_flips[new_flippable] = level
					new_flippables.append(new_flippable)
					
		to_flip = new_flippables
		if len(to_flip) == 0:
			level = None
	return all_flips

total_cases=int(input())
for num_case in range(1,total_cases+1):
    pancake,k_str = input().split()
    k = int(k_str)
    lst = pancakes_flipper(k,len(pancake))
    if pancake in lst:
        print("Case #{}: {}".format(num_case,lst.get(pancake)))
    else:
        print("Case #{}: IMPOSSIBLE".format(num_case))
