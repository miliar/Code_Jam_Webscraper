##### Functions Below ##########################################################
def get_deciet_score(naomi_tiles, ken_tiles):
	score = 0
	for i in range(len(naomi_tiles)):
		ken_highest = max(ken_tiles)
		naomi_winners = []
		for tile in naomi_tiles:
			if tile > ken_highest:
				naomi_winners.append(tile)
		if naomi_winners:
			naomi_tiles.remove(min(naomi_winners))
			ken_tiles.remove(ken_highest)
			score += 1
		else:
			naomi_tiles.remove(min(naomi_tiles))
			ken_tiles.remove(ken_highest)
	return score

def get_reg_score(naomi_tiles, ken_tiles):
	score = 0
	for i in range(len(naomi_tiles)):
		naomi_max = max(naomi_tiles)
		ken_winners = []
		ken_losers = []
		for tile in ken_tiles:
			if tile > naomi_max:
				ken_winners.append(tile)
			else:
				ken_losers.append(tile)
		if ken_winners:
			naomi_tiles.remove(naomi_max)
			ken_tiles.remove(min(ken_winners))
		else:
			naomi_tiles.remove(naomi_max)
			ken_tiles.remove(min(ken_tiles))
			score += 1
	return score

##### Program Logic Below ######################################################

#The filenames of the input and output files
input_path = r"C:\Users\Jake\Documents\~Programming Stuff\Google Code Jam\Competition\Qualification Round\Problem 4\input.txt"
output_path = r"C:\Users\Jake\Documents\~Programming Stuff\Google Code Jam\Competition\Qualification Round\Problem 4\output.txt"

#Read in the text from the input file
input_text = open(input_path, 'r')

#Determine the number of test cases by converting the first line to an int
test_cases = int(input_text.readline())

# Solve each case and output answer to a text file
output_text = open(output_path, 'w')
for i  in range(test_cases):
	num_tiles = int(input_text.readline())

	naomi_tiles = input_text.readline()
	naomi_tiles = naomi_tiles.split()
	naomi_tiles = [float(t) for t in naomi_tiles]

	ken_tiles = input_text.readline()
	ken_tiles = ken_tiles.split()
	ken_tiles = [float(t) for t in ken_tiles]

	n_t = [i for i in naomi_tiles]
	k_t = [i for i in ken_tiles]
	deciet_score = get_deciet_score(n_t, k_t)	
	n_t = [i for i in naomi_tiles]
	k_t = [i for i in ken_tiles]
	reg_score = get_reg_score(n_t, k_t)

	output_text.write("Case #%d: %d %d" %((i + 1), deciet_score, reg_score) + "\n")

output_text.close()
