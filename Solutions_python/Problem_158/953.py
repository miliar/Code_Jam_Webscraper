from pprint import pprint
from math import floor
import copy

#infile = open('input.txt', 'r')
infile = open('D-small-attempt1.in', 'r')
outfile = open('output.txt', 'w')

num_problems = int(infile.readline())

def output(text):
	print(text)
	global outfile
	outfile.write("%s\n" % text)

def solve_helper(x,r,c):
	possibilities = [[1,2,2,2,2,2],
			 [2,2,3,3,4,4],
			 [2,3,3,4,5,5],
			 [2,3,4,4,6,6],
			 [2,4,5,6,6,6],
			 [2,4,5,6,6,6]]
	if (r * c) % x > 0:
		return False
	if x > 6:
		return False
	if x > r and x > c:
		return False
	if possibilities[r-1][c-1] < x:
		return False
	return True
# True: Gabriel can place whatever piece
# False: Some pieces cause issues
def solve(x,r,c):
	if solve_helper(x,r,c):
		return 'GABRIEL'
	return 'RICHARD'

for i in range(num_problems):
	x,r,c = [int(x) for x in infile.readline().split(' ')]
	output("Case #%s: %s" % (i+1, solve(x,r,c)))

infile.close()
outfile.close()

