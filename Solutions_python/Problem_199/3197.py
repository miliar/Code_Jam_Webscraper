import itertools

with open('A-small-attempt1.in', 'r') as f:
	prob1 = f.readlines()

total = int(prob1[0])
happy = 0
down = 0
case = 0
flips = 0
total_pancakes = 0
answer = []

# run through the rest of the lines
for x in range(1, total+1): # 1,total+1
	# per run format contained at this level
	success_runs = []
	case = case + 1
	x = prob1[x].rstrip() # pancake_line string, remove newline
	pancake_line = x[:len(x)-2].strip() # remove K number
	total_pancakes = len(pancake_line) # find number of pancakes we are workin with
	k = int(x[len(x)-2:]) # number of pancakes that flipper can handle
	line_members = []
	for p in x[:len(x)-2]:
		line_members.append(p)
		if p == '-':
			down = down + 1
		elif p == '+':
			happy = happy + 1 ################## Set the shortcut conditions?

	# Now find all possibilities
	max_flips_possible = total_pancakes - (int(k) - 1)

	flip_path = []
	# first flip assignment, label by the starting index flip
	for u in range(max_flips_possible):
		if int(k) <= (total_pancakes-u): 
			flip_path.append(u) 

	original = line_members
	# permutations of all places to start trying to flip
	for n in list(itertools.permutations(flip_path)):
		pancake_line_try = [p for p in x[:len(x)-2]]
		# flip that section
		num_flips_done = 0
		for position in n:
			num_flips_done = num_flips_done + 1
			flip_tracker = 0
			for pancake in pancake_line_try[position:position + k]:
				if pancake == '-':
					pancake_line_try[position+flip_tracker] = '+'
				elif pancake == '+':
					pancake_line_try[position+flip_tracker] = '-'
				flip_tracker = 1 + flip_tracker
			# check if the flip means all smiley
			#print(pancake_line_try)
			check = 0
			for n in pancake_line_try:
				if n == '+':
					check = check + 1
			# if all smiles then , good!
			if check == total_pancakes:
				success_runs.append(num_flips_done)


	if len(success_runs) == 0:
		string = 'Case #' + str(case) + ': IMPOSSIBLE' + '\n'
		if(happy == total_pancakes):
			success = 0
			string = 'Case #' + str(case) + ': ' + str(success) + '\n'
	else:
		success = min(success_runs)
		if(happy == total_pancakes):
			success = 0
		string = 'Case #' + str(case) + ': ' + str(success) + '\n'

	#print(string)
	# reset per run
	happy = 0
	down = 0
	total_pancakes = 0
	answer.append(string)

with open('result1.txt', 'w')as k:
	for a in answer:
		k.write(a)

# Easy shortcuts:
# if k = 1, min flips = down pancakes
# if k = 0, impossible
# if k > num pancakes, impossible?
# if happy = total # pancakes

# import itertools
# n = itertools.permutations([1,2,3])
# list(n)