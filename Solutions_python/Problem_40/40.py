#!/usr/bin/python

import pprint

def storeResult(function):
	outputs = {}

	def f(*args):
		if args not in outputs:
			outputs[args] = function(*args)

		return outputs[args]

	return f

def buildTree(treeText, pos):
	# find start of node
	while treeText[pos] != '(':
		pos += 1

	pos += 1

	# skip whitespace
	while treeText[pos] == ' ':
		pos += 1

	probText = ''

	# read probability
	while treeText[pos] != ' ' and treeText[pos] != ')':
		probText += treeText[pos]
		pos += 1

	prob = float(probText)
	
	# skip whitespace
	while treeText[pos] == ' ':
		pos += 1

	# determine type of node
	if treeText[pos] == ')':
		return ((prob, None), pos + 1)

	feature = ''

	# determine feature
	while treeText[pos] != ' ':
		feature += treeText[pos]
		pos += 1
	
	pos = pos + 1

	(tree1, pos) = buildTree(treeText, pos)
	(tree2, pos) = buildTree(treeText, pos)
	
	# find end of node
	while treeText[pos] != ')':
		pos += 1

	return ((prob, feature, tree1, tree2), pos + 1)

def readInput():
	file = open('A-large.in')
	testCaseCount = int(file.readline().rstrip())

	testCases = []

	for i in range(0, testCaseCount):
		lineCount = int(file.readline().rstrip())
		lines = [file.readline().lstrip().rstrip() for i in range(0, lineCount)]
		treeText = ' '.join(lines)

		tree = buildTree(treeText, 0)[0]
		
		lineCount = int(file.readline().rstrip())
		lines = [file.readline().rstrip().split(' ')[2:] for i in range(0, lineCount)]
		
		testCases.append((tree, lines))

	return testCases

def calculateCuteProbability(tree, animals):
	for animal in animals:
		node = tree
		probability = node[0]

		while node[1] is not None:
			if node[1] in animal:
				node = node[2]
			else:
				node = node[3]
			probability *= node[0]

		print "%.7f" % probability

testCases = readInput()
caseNumber = 1

for testCase in testCases:
	print "Case #%s:" % caseNumber
	calculateCuteProbability(*testCase)

	caseNumber += 1
