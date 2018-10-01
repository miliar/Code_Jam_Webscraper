
def war(naomiBlocks, kenBlocks):
	score = len(naomiBlocks)
	for block in naomiBlocks:
		chosenKen = 1
		for kblock in kenBlocks:
			if kblock > block and kblock < chosenKen:
				chosenKen = kblock
		
		if chosenKen < 1:
			score -= 1
			kenBlocks.remove(chosenKen)
		else:
			kenBlocks.remove(min(kenBlocks))

	return score

def deceitfulWar(naomiBlocks, kenBlocks):
	score = 0
	for i in range(len(naomiBlocks)):
		minKen = min(kenBlocks)

		chosenNaomi = 1
		for block in naomiBlocks:
			if block < chosenNaomi and block > minKen:
				chosenNaomi = block
		if chosenNaomi < 1:
			naomiBlocks.remove(chosenNaomi)
			kenBlocks.remove(min(kenBlocks))
			score += 1
		else:
			naomiBlocks.remove(min(naomiBlocks))
			kenBlocks.remove(max(kenBlocks))

	return score



def main(filePath):
	answer = open('answers','w')
	with open(filePath, 'r') as f:
		numCase = int(float(f.readline().strip()))

		for i in range(numCase):
			numBlocks = int(float(f.readline().strip()))

			naomiBlocks = [float(x) for x in f.readline().strip().split()]
			kenBlocks = [float(x) for x in f.readline().strip().split()]

			deceitfulScore = deceitfulWar(list(naomiBlocks),list(kenBlocks))
			warScore = war(list(naomiBlocks),list(kenBlocks))

			answer.write('Case #%s: %s %s\n' % ((i+1),deceitfulScore,warScore))


if __name__ == '__main__':
	import sys
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		raise Exception('[-] Missing arg')