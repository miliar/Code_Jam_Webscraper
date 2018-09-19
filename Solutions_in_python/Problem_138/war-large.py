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




fo = open("D-large.in", "r+")
fw = FileWrapper(fo)


num_test_cases = fw.getInt()

for x in xrange(0, num_test_cases):

	num_block_each = fw.getInt()
	naomi_blocks = fw.getFloats()
	ken_blocks = fw.getFloats()

	

	naomi_blocks.sort()
	dirty_naomi_blocks = []
	i=0
	while i < len(naomi_blocks):
		dirty_naomi_blocks.append(naomi_blocks[i])
		i+=1

	ken_blocks.sort()
	dirty_ken_blocks = []
	i=0
	while i < len(ken_blocks):
		dirty_ken_blocks.append(ken_blocks[i])
		i+=1

	dirty_naomi_score = 0
	while len(dirty_naomi_blocks) > 0:
		length = len(dirty_naomi_blocks)

		if dirty_naomi_blocks[length-1] > dirty_ken_blocks[length-1]:
			dirty_naomi_score += 1
			del dirty_naomi_blocks[length-1]
			del dirty_ken_blocks[length-1]
		else:
			n_block = dirty_naomi_blocks[0]
			del dirty_naomi_blocks[0]
			k_block = dirty_ken_blocks[length-1]
			del dirty_ken_blocks[length-1]

			if n_block > dirty_ken_blocks:
				dirty_naomi_score += 1
	
	naomi_score = 0
	while len(naomi_blocks) > 0:
		length = len(naomi_blocks)

		n = length-1
		k = length-1

		if naomi_blocks[n] > ken_blocks[k]:
			k = 0

		elif (length > 1):
			n = length-2
			n_block = naomi_blocks[n]

			k=0
			while (ken_blocks[k] <= n_block) and (k < length-1):
				k+=1

		n_block = naomi_blocks[n]
		k_block = ken_blocks[k]
		if k_block <= n_block:
			k=0
			naomi_score += 1
		del naomi_blocks[n]
		del ken_blocks[k]


	print "Case #" + str(x+1) + ": " + str(dirty_naomi_score) + " " + str(naomi_score)

fw.close()
