class Reader:
	def __init__(self):
		self.cases = 0
		self.n = 0
	
	def open(self, inputname, outputname):
		self.input = open(inputname)
		self.output = open(outputname, 'w')
		self.cases = int(self.input.readline())
	
	def getCases(self):
		return self.cases
	
	def out(self, line):
		print 'Case #' + str(self.n + 1) + ': ' + line
		self.output.write('Case #' + str(self.n + 1) + ': ' + line + '\n')
		self.n += 1
	
	def close(self):
		self.input.close()
		self.output.close()

	def readLine(self, delimiter = None):
		if delimiter == None:
			return self.input.readline().strip()

		return self.input.readline().strip().split(delimiter)

	def readLines(self, num, delimiter = None):
		temp = []
		for i in range(0, num):
			if delimiter == None:
				temp.append(self.input.readline().strip())
			else:
				temp.append(self.input.readline().strip().split(delimiter))
		return temp

r = Reader()
r.open("A-small-attempt0.in", "A-small-attempt0.out")

cases = r.getCases()
vowels  = ['a', 'e', 'i', 'o', 'u']

def hasCC(word, n):
	k = 0
	
	for l in word:
		if (l in vowels) == False:
			k += 1
		else:
			k = 0
		if k == n : return True
	return False

def countCC(word, n):
	limit1 = len(word)
	w = 0
	
	for u in range(0, limit1):
		for v in range(1 + u, limit1 + 1):
			if hasCC(word[u:v], n) : w += 1
	return w

def solveCase(i):
	cucli = r.readLine(' ')
	word = cucli[0]
	n = int(cucli[1])
	w = countCC(word, n)
	
	return str(w)

for i in range(0, cases):
	r.out(solveCase(i))

r.close()
