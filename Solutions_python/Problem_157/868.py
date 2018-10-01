# ================ UTILS START =========================
Case = 0
def readAndExecute(filename, testBlockSize, testFunction):
	with open(filename) as f: 
		T = int(f.readline().strip())
		for t in xrange(T):
			lines = []
			for l in xrange(testBlockSize):
				lines.append(f.readline().strip())
			testFunction(lines)

def formatAnswer(answer):
	global Case
	Case += 1 
	return "Case #"+ str(Case) + ": " + str(answer)

# ================ UTILS END =========================
quaternions = [
	["1", "i", "j", "k"],
	["i", "-1", "k", "-j"],
	["j", "-k", "-1", "i"],
	["k", "j", "-i", "-1"],
	["-1", "-i", "-j", "-k"],
	["-i", "1", "-k", "j"],
	["-j", "k", "1", "-i"],
	["-k", "-j", "i", "1"],
]
def multiply(a, b):
	sign = 1
	if a[0] == '-':
		a = a[1]
		sign *= -1
	if b[0] == '-':
		b = b[1]
		sign *= -1
	row = 0
	col = 0
	if sign == -1:
		row += 4
	if a == "i":
		row += 1
	elif a == "j":
		row += 2
	elif a == "k":
		row += 3

	if b == "1":
		col = 0
	elif b == "i":
		col = 1
	elif b == "j":
		col = 2
	elif b == "k":
		col = 3
	return quaternions[row][col]

def dijkstra(lines):
	L = int(lines[0].split(" ")[0])
	X = int(lines[0].split(" ")[1])
	string = lines[1] * X
	if len(string) < 3:
		return False
	if string == "ijk":
		return True


	#find first occurrence of i
	index = 0
	product = "1"
	i_run_start = None
	i_run_end = None
	while index < len(string):
		product = multiply(product, string[index])
		if product == "i":
			i_run_start = 0
			i_run_end = index
			index += 1
			break
		index += 1
	if i_run_end is None:
		return False



	#find all runs of j
	jstack = []
	p = "1"
	while index < len(string):
		p = multiply(p, string[index])
		if p == "j":
			jstack.append(index)
		index += 1
	if len(jstack) == 0:
		return False

	for index in jstack:
		index += 1
		p = "1"
		while index < len(string):
			p = multiply(p, string[index])
			index += 1
		if p == "k" and index == len(string):
			return True


def run(lines):
	if dijkstra(lines):
		print formatAnswer("YES")
	else:
		print formatAnswer("NO")

readAndExecute("C-small-attempt0.in", 2, run)
