from pprint import pprint
import copy

infile = open('C-small-attempt0.in', 'r')
#infile = open('input.txt', 'r')
outfile = open('output.txt', 'w')

num_problems = int(infile.readline())

def output(text):
	print(text)
	global outfile
	outfile.write("%s\n" % text)

def isleft(p1,p2,p3):
	return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])

def solve(trees):
	if(len(trees) == 1):
		output(0)
		return
	for i in range(len(trees)):
		minimum = 3000
		for j in range(len(trees)):
			if i != j:
				side1 = 0
				side2 = 0
				online = 0
				for tree in trees:
					position = isleft(trees[i],trees[j],tree)
					if position > 0:
						side1 = side1 + 1
					if position < 0:
						side2 = side2 + 1
					if position == 0:
						online = online + 1
				if minimum > len(trees) - (max(side1,side2)+online):
					minimum = len(trees) - (max(side1,side2)+online)
		output(minimum)

for i in range(num_problems):
	numtrees = int(infile.readline())
	trees = []
	for j in range(numtrees):
		trees.append([int(x) for x in infile.readline().rstrip('\n').split(' ')])
	output("Case #%s:" % (i+1))
	solve(trees)

infile.close()
outfile.close()

