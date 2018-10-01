from __future__ import print_function
import sys



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
				d, n = line.split(' ')
				d, n = int(d), int(n)
				max_time = 0
				for i in xrange(int(n)) :
					line = next(fin)
					k, s = line.split(' ')
					k, s = int(k), int(s)
					time = 1.0*(d-k)/s
					if time > max_time:
						max_time = time
					


				print('Case #%d: %f' % (cnt, d/max_time))
				cnt += 1
