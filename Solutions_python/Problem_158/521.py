from string import *
import math

def read_words(filename):
    '''
    converts a file to a list
    '''
    words = []
    for line in filename:
            words.append(line.strip())
    return words

filename = open("in.txt", 'r')
numcases = int(filename.readline().split()[0])

for case in range(numcases):
	info = filename.readline().split()
	x = int(info[0])
	r = int(info[1])
	c = int(info[2])
	gabe = True

	if (r*c == 0): #r or c zero... this could happen!
		gabe = False
	elif not ((r*c) % x == 0):
		gabe = False
	elif (x>4): # for small input ONLY!!!!!!
		gabe = False
	elif (x == 1):
		gabe = True
	elif (x == 2):
		gabe = ((r*c)%2 == 0) # if odd by odd, rich wins, else loss
	elif (x == 3):
		gabe = (min(r,c) >=2)
	elif (x == 4):
		gabe = ((r*c)%4 == 0 and (min(r,c) >=3))
	#elif (x == 5):
	#	gabe = (min(r,c) >=3)

	if not gabe:
		print "Case #" + str(case+1) + ": " + "RICHARD"
	else:
		print "Case #" + str(case+1) + ": " + "GABRIEL"