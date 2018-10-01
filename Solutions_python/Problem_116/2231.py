"""

code jam
Qualification Round 2013
Problem A. Tic-Tac-Toe-Tomek

"""
import time
start = time.time()

in_file = open('input/alarge.txt', 'r')
out_file = open('output/alarge.txt', 'w')

def tcount(s):
	outlist = [s.count('X'), s.count('O'), s.count('T')]
	if outlist[0] == 4:
		return 'X'
	elif outlist[1] == 4:
		return 'O'
	else:
		if outlist[2] == 1:
			if outlist[0] == 3:
				return 'X'
			elif outlist[1] == 3:
				return 'O'
	return None

def my_method(inlist):
	collist = ['','','','']
	olist = []
	for e in inlist:
		collist[0] += e[0]
		collist[1] += e[1]
		collist[2] += e[2]
		collist[3] += e[3]
		olist.append(e)
	
	olist.append(inlist[0][0] + inlist[1][1] + inlist[2][2] + inlist[3][3])
	olist.append(inlist[0][3] + inlist[1][2] + inlist[2][1] + inlist[3][0])
	
	#print collist, ulist
	for e in collist:
		olist.append(e)
	#print "OLIST = ", olist

	for e in olist:
		#print tcount(e)
		if tcount(e) == 'X':
			return 'X won'
		elif tcount(e) == 'O':
			return 'O won'

	for e in olist:
		#print e
		if '.' in e:
			return 'Game has not completed'
	
	return 'Draw'

#print tcount('...X')
#my_method(['OOXO', 'XOXX', 'OOXT', '...X'])

testcases = int(in_file.readline())

i = 1
while i <= testcases:
	inlist = []
	inlist.append(in_file.readline()[:-1])
	inlist.append(in_file.readline()[:-1])
	inlist.append(in_file.readline()[:-1])
	inlist.append(in_file.readline()[:-1])
	in_file.readline()
	#print i, inlist
	result = my_method(inlist)
	#print result
	outline = "Case #" + str(i) + ": " + str(result)
	print >> out_file, outline

	i += 1

in_file.close()
out_file.close()

print "Elapsed time is " +  str(time.time() - start)