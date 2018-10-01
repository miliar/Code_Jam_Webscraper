import math

def checka_right(list, index):
	count = 0
	while(list[index + count + 1] != -1):
		count += 1
	return count

def checka_left(list, index):
	count = 0
	while(list[index + count - 1] != -1):
		count -= 1
	return -count

with open("C-small-1-attempt0.in") as f:
	content = f.readlines()
content = [x.strip() for x in content] 

num_probs = int(content[0])
probs = []

for i in range(1, num_probs+1):
	probs.append(content[i].split(" "))

for i in range(0, num_probs):
	free_stalls = int(probs[i][0])
	persons = int(probs[i][1])
	stalls = []
	stalls.append(-1)
	free_stalls -= 1
	for stall in range(1, free_stalls+2):
		stalls.append(free_stalls)
		free_stalls -= 1
	stalls.append(-1)
	for person in range(persons-1):
		max_value = max(stalls)
		index = stalls.index(max_value)
		choice = int(math.floor(float(max_value)/2))
		stalls[choice + index] = -1
		for idx in range(index, index + choice):
			stalls[idx] = choice - 1
			choice -= 1
	max_value = max(stalls)
	index = stalls.index(max_value)
	choice = int(math.floor(float(max_value)/2))
	stalls[index + choice] = -1
	Ls = checka_left(stalls, index + choice)
	Rs = checka_right(stalls, index + choice)
	print "Case #{}: {} {}".format(i+1, max([Ls, Rs]), min([Ls, Rs]))

