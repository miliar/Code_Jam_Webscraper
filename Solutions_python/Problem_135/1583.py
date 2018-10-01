class FileWrapper:
    def __init__(self, file):
        self.file = file
    
    def getInt(self):
        return int(self.file.readline())
    
    def getInts(self):
        return [int(z) for z in self.file.readline().split()]
    
    def getFloat(self):
        return float(self.file.readline())
    
    def getFloats(self):
        return [float(z) for z in self.file.readline().split()]
    
    def getWords(self):
        return self.file.readline().split()
    
    def readline(self):
        return self.file.readline().strip()
    
    def close(self):
        self.file.close



def matching_ints(ints1, ints2):
	matching = []
	for i in range(0, len(ints1)):
		for j in range (0, len(ints2)):
			if (ints1[i] == ints2[j]):
				matching.append(ints1[i])
	return matching


fo = open("A-small-attempt0.in", "r+")
fw = FileWrapper(fo)


intput_line = 0

num_test_cases = fw.getInt()

for x in xrange(0, num_test_cases):
	first_answer = fw.getInt()
	first_card_grid = []
	first_card_grid.append(fw.getInts());
	first_card_grid.append(fw.getInts());
	first_card_grid.append(fw.getInts());
	first_card_grid.append(fw.getInts());

	possible_cards = first_card_grid[first_answer-1]

	second_answer = fw.getInt()
	second_card_grid = []
	second_card_grid.append(fw.getInts());
	second_card_grid.append(fw.getInts());
	second_card_grid.append(fw.getInts());
	second_card_grid.append(fw.getInts());

	matches = matching_ints(possible_cards, second_card_grid[second_answer-1])

	if len(matches) == 1:
		print "Case #" + str(x+1) + ": " + str(matches[0])
	elif len(matches) == 0:
		print "Case #" + str(x+1) + ": Volunteer cheated!"
	else:
		print "Case #" + str(x+1) + ": Bad magician!"







fw.close()
