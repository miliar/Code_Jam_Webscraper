
from copy import deepcopy

import math

if __name__ == '__main__':

	t = int(raw_input()) 
	for k in xrange(1, t + 1):
		raw = raw_input()

		N, R, O, Y, G, B, V = map(int, raw.split(' ')) 

		# print N

		colors = [
			('R', R),
			('O', O),
			('Y', Y),
			('G', G),
			('B', B),
			('V', V)
		]

		result = ''

		for c, n in colors:
			if float(n) > math.floor(float(N)/2) : 
				result = 'IMPOSSIBLE'
				break

		colors = sorted(colors, key=lambda tup: tup[1], reverse=True)

		if result != 'IMPOSSIBLE':

			# print result

			res = []

			for i, (c, n) in enumerate(colors):
				if i == 0:
					for j in xrange(n):
						res.append(c)
				else:
					count = n
					while count > 0:

						added = False

						for j in xrange( len(res) ):
							# print j, len(res)
							if (j) == len(res)-1 :
								# print 'a'
								if (res[j] == res[0]):
									res.insert(0, c)
									count = count - 1
									added = True
									break
							else:
								# print 'b'
								if res[j] == res[j+1]:
									res.insert(j+1, c)
									count = count - 1
									added = True
									break

						if not added :
							for j in xrange( len(res) ):
								# print j, len(res)
								if (j) == len(res)-1 :
									# print 'a'
									if (res[j] != c) & (res[0] != c):
										res.insert(0, c)
										count = count - 1
										break
								else:
									# print 'b'
									if (res[j] != c) & (res[j+1] != c):
										res.insert(j+1, c)
										count = count - 1
										break

						
						pass


			for r in res:
				result = result + r

			# while True:

			# 	finish = True

			# 	for c, n in colors:
			# 		if n != 0: 
			# 			finish = False
			# 			break 

			# 	if finish : break


			# 	# print colors
				
			# 	for i, (c, n) in enumerate(colors):

			# 		if n > 0:

			# 			result = result + c
			# 			colors[i] = (c, n-1)


		# if result == 10000000000:
		# 	print 'Case #{}: {}'.format(k, 'IMPOSSIBLE')
		# else:
		print 'Case #{}: {}'.format(k, result)

