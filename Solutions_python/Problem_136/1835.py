# !/usr/bin/python2.7
# -*- coding:utf-8 -*-

# By: Vasanthi Vuppuluri
# Last modified date: April 12, 2014

import os

def main():
	T = raw_input()
	T = int(T)
	
	global Output
	Output = []		

	if (1 <= T <= 100):
		
		for Case in xrange(0,T):
			input_line = raw_input()
			input_line = input_line.split()
			
			if (len(input_line) == 3):
				C = float(input_line[0])
				F = float(input_line[1])
				X = float(input_line[2])

			# Number of cookies gained per second - initially
			cookies = 2

			# Time to produce X cookies without buying any cookie factories
			wait_time = X / cookies
			
			# Time to buy first factory
			buy_time = 0.0
			
			while (1):
				buy_time = buy_time + (C / cookies)
				new_cookies = cookies + F
				new_buy_time = buy_time + (X / new_cookies)
				cookies = new_cookies
				if (new_buy_time > wait_time):
					time = 'Case #%d: %f' %(Case+1, wait_time)
					Output.append(time)
					break
				else:
					wait_time = new_buy_time
					new_buy_time = 0.0
				
		ofile = 'Output.txt'

		if os.path.isfile(ofile):
			os.remove(ofile)
			
		ofile = open(ofile,'a')

		for op in Output:
			ofile.write(op)
			ofile.write('\n')

		ofile.close()


if __name__ == "__main__":
    main()