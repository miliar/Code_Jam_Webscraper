import os
import sys
import math
import operator

if __name__ == "__main__":
	in_handle = open("B-small-attempt0.in","r");
	test_case_count = int(in_handle.readline())
	test_case_counter = 0;
	while(test_case_counter<test_case_count):
		destructive_dict = {}
		constructive_dict = {}
		destructive_list = []
		
		#print"-"*100
		#prepareing constructive dict
		input = in_handle.readline().split()
		position = 0;
		end_term = int(input[position])
		for counter in range(0, end_term):
			position= position+1;
			constructive_dict[input[position][0]]=(input[position][1],input[position][2])
			if(input[position][0] != input[position][1]):
				constructive_dict[input[position][1]]=(input[position][0],input[position][2])
			
		position = position+1;
		#preparing destructive dict
		end_term = int(input[position])
		for counter in range(0, end_term):
			position = position+1;
			destructive_dict[input[position][0]] =input[position][1] 
			if(input[position][0] != input[position][1]):
				destructive_dict[input[position][1]] =input[position][0]
			
		#print constructive_dict
		#print destructive_dict
		position = position+1;
		end_term = int(input[position])
		position = position +1
		prev_char = '1'
		my_list = []
		for counter in range(0, end_term):
			current_char = input[position][counter]
			#print current_char
			#checking reconstructuion
			if(constructive_dict.has_key(current_char)):
				if(constructive_dict[current_char][0] == prev_char):
					my_list.pop()
					my_list.append(constructive_dict[current_char][1]);
					prev_char = constructive_dict[current_char][1];
					#print "comming in construction"
					#print my_list
					continue;
			#checking destruction
			if(destructive_dict.has_key(current_char)):
				if(destructive_dict[current_char] in my_list):
					my_list = []
					prev_char = '1';
					#print "comming in destruction"
					#print my_list
					continue;
			my_list.append(current_char);
			prev_char = current_char
			#print my_list
		
		print "Case #%d: [%s]"%(test_case_counter+1, ", ".join(my_list))
		test_case_counter = test_case_counter+1
					