#!/usr/bin/python

import fileinput

line_cnt=0
test_cases=1
set1=set()
set2=set()

for line in fileinput.input():
	if(line_cnt > (test_cases*10)):
		#print 'error'
		break;
	#print str(line_cnt) + 'c' + str(line_cnt%10)
	#print line.rstrip() + 'l'
	if(line_cnt == 0):
		test_cases=int(line.rstrip());
		#print test_cases
	elif((line_cnt % 10) ==1):
		first_row=int(line.rstrip());
		#print str(first_row) + ' first'
	elif((line_cnt % 10) ==6):
		second_row=int(line.rstrip());
		#print str(second_row) + ' second'
	elif(((line_cnt%10) > 1) and ((line_cnt%10) < 6)):
		first_arrangement=(line.rstrip());
		#print str(first_arrangement) + 'f'
		#print str((line_cnt%10)-1) + 'fc'
		if(((line_cnt%10)-1) == first_row):
			set1=set(first_arrangement.split());
			#print 'remember:'+first_arrangement+'f';
	elif((((line_cnt-1)%10) > 5) and (((line_cnt-1)%10) <= 9)):
		second_arrangement=(line.rstrip());
		#print str(second_arrangement) + 's'
		#print str(((line_cnt-1)%10)-5) + 'sc'
		if((((line_cnt-1)%10)-5) == second_row):
			set2=set(second_arrangement.split());
			#print 'remember:' + second_arrangement+'s';
		if(((line_cnt-1)%10)==9):
			common=set1.intersection(set2);
			#print common;
			common_cards=len(common)
			if(common_cards==1):
				for i in common:
					print 'Case #' + str(line_cnt/10) + ': ' + i;
			elif(common_cards == 0):
					print 'Case #' + str(line_cnt/10) + ': Volunteer cheated!';
			else:
					print 'Case #' + str(line_cnt/10) + ': Bad magician!';
	line_cnt+=1;
