import os
import sys
import math



if __name__=="__main__":
		in_handle = open("A-large.in", "r");
		test_case_count = int(in_handle.readline());
		global_number=1;
		while(global_number<test_case_count+1):
			travel_list = in_handle.readline().split()
			orange_counter = 0;
			blue_counter=0;
			previous_blue_button= 1;
			previous_orange_button = 1;
			global_counter=0;
			#global orange_counter,blue_counter,previous_blue_button,previous_orange_button,global_counter
			counter = 1;
			#print travel_list
			while(counter < int(travel_list[0])*2):
				distance = int(travel_list[counter+1])
				if (travel_list[counter] == 'B') :
					moves = abs(distance-previous_blue_button);
					blue_counter = blue_counter + moves+1;
					global_counter = global_counter + 1;
					blue_counter = (blue_counter ,global_counter)[blue_counter<global_counter];
					global_counter = blue_counter;
					previous_blue_button = distance;
				if (travel_list[counter] == 'O') :
					moves = abs(distance-previous_orange_button);
					orange_counter = orange_counter + moves+1;
					global_counter = global_counter + 1;
					orange_counter = (orange_counter ,global_counter)[orange_counter<global_counter];
					global_counter = orange_counter;
					previous_orange_button = distance;
					#print travel_list[counter], travel_list[counter+1],counter, travel_list[0];
				counter = counter + 2;
			print "Case #%d: %d" %(global_number, global_counter)
			global_number= global_number+1


