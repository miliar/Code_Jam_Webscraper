import sys 
import string
from collections import *

def intersect(a, b):
	return list(set(a) & set(b))

f = open(sys.argv[1])

T = int(f.readline())
for c in xrange(1, T+1): 
	firstanswer = int(f.readline())
	for r in xrange(1, firstanswer+1):
		row1 = f.readline().strip().split(' ')
	for r in xrange(firstanswer, 4):
	 f.readline()
	secondanswer = int(f.readline())
	for r in xrange(1, secondanswer+1):
		row2 = f.readline().strip().split(' ')
	for r in xrange(secondanswer, 4):
		f.readline()
	inter = intersect(row1, row2)
	if len(inter)==1:
	   answer = inter[0]
	elif len(inter)<1:
	   answer = 'Volunteer cheated!'
	else: answer = 'Bad magician!'
	print 'Case #' + str(c) + ': ' + answer
	

