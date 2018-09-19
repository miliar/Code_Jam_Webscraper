import sys
import re

input_arr = []
num_input = 0

# first_ans_arr = []
first_ans_poss = []

# second_ans_arr = []
second_ans_poss = []

ans_arr = []

def read_file():

	with open("jamq1i.txt", 'r') as f:
		count = 0
		for line in f:
			# print "hi"
			if count == 0:
				num_input = int(line[:-1])
			else:
				input_arr.append(line[:-1])
			# if (count - 1) % 10 == 0:
			# 	first_ans = int(line[:-1])
			# else if (count - 1) % 10 == first_ans:
			# 	first_ans_poss.append(line[:-1].split())

			# if (count - 1) % 10 == 5:
			# 	second_ans = int(line[:-1])
			# input_arr.append(int())
			count+=1

	f.close()
def parse_stuff():
	# print input_arr

	for x in xrange(0, len(input_arr), 10):
		first_ans = int(input_arr[x])
		first_poss = input_arr[x+first_ans].split()
		
		second_ans = int(input_arr[x+5])
		second_poss = input_arr[x+5+second_ans].split()
		count = 0
		for ele in first_poss:
			if ele in second_poss:
				count+=1;
		# print first_poss
		# print second_poss
		if count == 0:
			# print 0
			ans_arr.append("Volunteer cheated!")
		if count == 1:
			# print 1
			for ele in first_poss:
				if ele in second_poss:
					ans_arr.append(int(ele))
		if count >= 2:
			# print count
			ans_arr.append("Bad magician!")


def main():
	read_file()
	parse_stuff()
	# print ans_arr

	with open("jamq1o.txt", 'w') as f:
		for x in xrange(len(ans_arr)):
			f.write('Case #' + str(x+1) + ": " + str(ans_arr[x]) + '\n')
	f.close() 
main()