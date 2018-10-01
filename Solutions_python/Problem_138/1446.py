input = open("4input", "r")
output = open("4output", "w")

def readline():
	return input.readline()

def writeline(string):
	output.write(string + "\n")

class Player():

	def choose_move(self):
		return None

class Naomi(Player):

	def __init__(self, blocks, blocks_other):
		self.blocks = blocks
		self.other = blocks_other
		self.pts = 0

	def choose_move(self):
		return self.blocks.pop(0)

	def choose_move_deceitful(self):
		if len(self.blocks) == 0:
			thing = self.blocks.pop(0)

			return [thing, thing]

		if self.blocks[0] < self.other[0]:
			thing = self.blocks.pop(0)

			return [thing, self.other[len(self.other) - 1] - .00001]

		if self.blocks[0] > self.other[0]:
			if self.blocks[len(self.blocks) - 1] > self.other[len(self.other) - 1]:
				thing = self.blocks.pop(len(self.blocks) - 1)

				return [thing, thing]

			thing = self.blocks.pop(0)

			return [thing, self.other[len(self.other) - 1] - .00001]

		

class Ken(Player):

	def __init__(self, blocks):
		self.blocks = blocks
		self.pts = 0

	def choose_move(self, other):
		for i in range(len(self.blocks)):
			if self.blocks[i] > other:
				return self.blocks.pop(i)

		return self.blocks.pop()

def play_war(naomi_blocks, ken_blocks):
	nao = Naomi(naomi_blocks, ken_blocks)
	ken = Ken(ken_blocks)

	while len(ken.blocks) > 0:
		m1 = nao.choose_move()
		m2 = ken.choose_move(m1)

		if m1 > m2:
			nao.pts += 1
		else:
			ken.pts += 1

	return nao.pts

def play_deceitful_war(naomi_blocks, ken_blocks):
	nao = Naomi(naomi_blocks, ken_blocks)
	ken = Ken(ken_blocks)

	while len(ken.blocks) > 0:
		m1 = nao.choose_move_deceitful()
		m2 = ken.choose_move(m1[1])

		if m1[0] > m2:
			nao.pts += 1
		else:
			ken.pts += 1

	return nao.pts


def main():
	count = int(readline())
	for x in range(count):
		i = int(readline())

		naomi_blocks = map(float, readline().replace(" \n", "").replace("\n", "").split(" "))
		naomi_blocks.sort()
		ken_blocks = map(float, readline().replace(" \n", "").replace("\n", "").split(" "))
		ken_blocks.sort()

		pts1 = play_war(naomi_blocks[:], ken_blocks[:])
		pts2 = play_deceitful_war(naomi_blocks, ken_blocks)

		writeline("Case #" + str(x + 1) + ": " + str(pts2) + " " + str(pts1))

main()
