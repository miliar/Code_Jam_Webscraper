from __future__ import print_function

import sys

def cutCake(input):

	r = len(input)
	c = len(input[0])

	# print input
	for rr in xrange(r):
		for cc in xrange(c):
			# print rr, cc

			i, j = rr, cc
			while(input[i][j] != '?' and  j+1 < c and input[i][j+1]=='?'):
				input[i][j+1] = input[i][j]
				j += 1

			i, j = rr, cc
			while(input[i][j] != '?' and j-1 >=0 and input[i][j-1]=='?'):
				input[i][j-1] = input[i][j]
				j -= 1
	
	# print "1st", input


	for rr in xrange(r):
		for cc in xrange(c):
			i, j = rr, cc
			while(input[i][j] != '?' and i+1 < r and input[i+1][j]=='?'):
				input[i+1][j] = input[i][j]
				i += 1

			i, j = rr, cc
			while(input[i][j] != '?' and i-1 >=0 and input[i-1][j]=='?'):
				input[i-1][j] = input[i][j]
				i -= 1

	# print input
	# print 'done'
	return input


# here start the main program
if __name__=='__main__':
	cases = -1
	cnt = 1
	file = sys.argv[1]

	rem = 0

	# open the file and call the largest tidy number and valid tidy number
	with open(file) as fin:
		for line in fin:
			if cases == -1:
				cases = line
			else:
				# print line
				r, c = line.split(' ')
				input = []
				for i in xrange(int(r)) :
					line = next(fin)
					input.append([])
					for j in xrange(int(c)):
						input[i].append( line[j] )
					

				res = cutCake(input)

				print('Case #%d:' % (cnt))
				for i in xrange(len(res)):
					for j in xrange(len(res[0])):
						print(res[i][j], end='')
					print("")
				cnt += 1
