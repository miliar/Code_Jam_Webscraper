from operator import itemgetter
from decimal import Decimal
import sys
import time

def main(argv):
	''' The main function '''
	#open the file
	with open(argv[1]) as f:
		#number of testcases
		T = int(f.readline().rstrip())
		lines = iter(f.readlines())

		for i in xrange(1, T + 1):

			n = int(str(lines.next()).rstrip())
			n_list = map(float, lines.next().rstrip().split(" "))
			k_list = map(float, lines.next().rstrip().split(" "))

			#war
			n_list = sorted(n_list)
			k_list = sorted(k_list)

			n_index = 0
			k_index = 0
			flag = True

			while flag:
				while k_index < n and k_list[k_index] < n_list[n_index]:
					k_index += 1
				if k_index >= n:
					break

				k_index += 1
				n_index += 1

			result1 = n - n_index

			#deceitful war
			k_index = n - 1
			n_index = n - 1

			

			while k_index >= 0:
				#find a fake value greater than second largest element in ken 
				# but lesser than largest element 
				#also, shouldnt exist in naomi list

				# n_high_list = [x for x in n_list if x > k_list[k_index - 1]]
				# n_high_list = [x for x in n_high_list if x < k_list[k_index]]

				# fake_value = k_list[k_index] - 0.0000001
				# while fake_value > k_list[k_index - 1]:
				# 	if fake_value not in n_high_list:
				# 		#found
				# 		break
				# 	fake_value -= 0.0000001

				#fake value HAS to be found.. 
				# so just decrement k_index and increment n_index

				if n_list[n_index] > k_list[k_index]:
					n_index -= 1

				# print n_index
				# print n
				k_index -= 1

				

			result2 = n - n_index - 1

			print "Case #%d: %d %d" % (i, result2, result1)
			

if __name__ == "__main__":
	main(sys.argv)