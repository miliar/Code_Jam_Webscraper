from __future__ import with_statement
import sys

def readInt(f):
	return int(f.readline().strip())

def buildTree(words):
	tree = {}

	for word in words:
		current = tree
		for letter in word:
			if letter in current:
				current = current[letter]
			else:
				current[letter] = {}
				current = current[letter]
	
	return tree

def recurseSolve(tree, components):
	if not components:
		#end of our search space
		return 1

	first = components[0]

	total = 0

	for letter in first:
		if letter not in tree:
			continue
		else:
			total += recurseSolve(tree[letter], components[1:])

	return total

def solve(tree, case):
	#split the case into it's components
	components = []
	component = ""
	inChoice = False

	for letter in case:
		if letter == "(":
			inChoice = True
		elif letter == ")":
			components.append(component)
			component = ""
			inChoice = False
		else:
			if inChoice:
				component += letter
			else:
				components.append(letter)
	
	return recurseSolve(tree, components)

if __name__ == "__main__":
	file = sys.argv[1]
	output = "%s.out" % (file, )

	answers = []

	with open(file) as f:
		l, d, n = [int(foo) for foo in f.readline().strip().split(" ")]

		words = []
		for word in xrange(d):
			words.append(f.readline().strip())

		tree = buildTree(words)

		for case in xrange(n):
			case = f.readline().strip()

			answers.append(solve(tree, case))

	i = 0
	with open(output, 'w') as f:
		for answer in answers:
			i += 1
			f.write("Case #%s: %s\n" % (i, answer))
			print "Case #%s: %s" % (i, answer)
