f = open("oversizedPancakeFlipperLarge.in", "r")
new_file = open("oversizedPancakeFlipperLargeSol", "w")
t = int(f.readline())

def min_number_flips(pancakes, n):
	print pancakes
	pancakes_list = list(pancakes)
	if '-' not in pancakes_list:
		return 0
	current_flips = 0
	position = 0
	while len(pancakes) - position >= n:
		position = pancakes_list.index('-')
		if len(pancakes) - position < n:
			return "IMPOSSIBLE"
		for i in range(position, position + n):
			pancakes_list[i] = '+' if pancakes_list[i] == '-' else '-' 
		current_flips += 1
		if '-' not in pancakes_list:
			return current_flips
	return "IMPOSSIBLE"

for i in range(1,t+1):
	pancakes , n = f.readline().split(' ')
	new_file.write("Case #"+str(i)+ ": "+str(min_number_flips(pancakes, int(n)))+"\n")