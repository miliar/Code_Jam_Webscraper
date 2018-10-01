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

			cfx = map(float, lines.next().rstrip().split(" "))

			c = cfx[0]
			f = cfx[1]
			x = cfx[2]
			
			current_speed = 2
			time_required_to_reach_C_at_current_rate = 0

			flag = True

			# print c, f, x
			while flag:
				time_required_to_reach_C_at_current_rate += c/current_speed
				remaining_cookies = x - c
	
				#compare time taken to get cookies at current_spped with 
				#time taken to remove C cookies nd buy a farm nd get cookies 
				#at (current_speed + F)

				if remaining_cookies/current_speed > x/(current_speed + f):
					current_speed += f

				else:
					final_time = time_required_to_reach_C_at_current_rate
					final_time += remaining_cookies/current_speed
					flag = False
		

			print "Case #%d: %s" % (i, format(Decimal(final_time),'.7f'))
			

if __name__ == "__main__":
	main(sys.argv)