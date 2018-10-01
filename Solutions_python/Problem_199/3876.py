explored = []
frontier = []
def solve(s, k, p=0):
	global explored
	global frontier
	"""
	s: A string of pancakes ---+-++-
	k: The size of your pancake flipper
	p: path depth
	return: 0..n if possible or IMPOSSIBLE
	"""
	explored.append(s)
	frontier.append(Node(s, None))

	while frontier:
		# fetch first item from queue
		item = frontier.pop()
		# check for goal condition
		if isHappy(item.string):
			explored = []
			frontier = []
			parent = item.parent
			while parent:
				p += 1
				parent = parent.parent
			return p
		# traverse childs
		for sn in childs(item.string, k):
			if sn not in explored:
				frontier.insert(0, Node(sn,item))
				explored.append(sn)

	frontier = []
	explored = []
	return "IMPOSSIBLE"

class Node:
	def __init__(self, string, parent):
		self.string = string
		self.parent = parent

def childs(s, k):
	c = []
	for i in range(0, len(s)-k+1):
		sn = s
		for x in range(0, k):
			sn = flip(sn, i + x)
		c.append(sn)
	return c

def test_childs():
	assert childs("+", 1) == ["-"]
	assert childs("++", 1) == ["-+", "+-"]
	assert childs("+++", 1) == ["-++", "+-+", "++-"]
	assert childs("+++", 2) == ["--+", "+--"]
	print(childs("+----++-", 5))
	assert childs("+----++-", 5) == ["-++++++-", "+++++-+-", "+-+++---", "+--++--+"]

def flip(s, i):
	c = s[i]
	if c is "-":
		c = "+"
	else:
		c = "-"
	return s[:i] + c + s[i+1:]

def test_flip():
	assert flip("+", 0) == "-"
	assert flip("+-", 0) == "--"
	assert flip("-+", 0) == "++"
	assert flip("---", 2) == "--+"
	assert flip("---", 1) == "-+-"
	assert flip("-+-", 1) == "---"

def isHappy(s):
	return "-" not in s

def main():
	# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
	# This is all you need for most Google Code Jam problems.
	t = int(input())  # read a line with a single integer
	for i in range(1, t + 1):
	  s, k = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
	  solution = solve(s,int(k))
	  print("Case #%d: %s" % (i, solution))

if __name__ == '__main__':
	main()