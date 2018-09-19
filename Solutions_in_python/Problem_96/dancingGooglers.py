

import sys
import string
import re




def is_best_possible( total_score , best_score ):
		
	
	min_score = (total_score - best_score)/2;
	
	#print best_score , min_score
	
	if min_score < 0:
		return False,False
		
	if best_score - min_score > 2:
		return False ,False;
	else:
		if best_score - min_score == 2 :
			return True, True
		else:
			return True, False


def get_best_dancer_count( surprises_allowed , best_score, scores ):

	
	
	best_with_surprises = 0;
	best_without_surprises = 0;

	for score in scores:
		is_best , is_surprise_used =  is_best_possible( score, best_score );
		#print is_best , is_surprise_used , score, best_score
		if is_best: 
			if is_surprise_used:
				best_with_surprises = best_with_surprises + 1;
			else:
				best_without_surprises = best_without_surprises + 1;
				
				
	return best_without_surprises + min ( best_with_surprises , surprises_allowed) ;



def solve_problem(input_file_path , output_file_path):
	
	input_file = open(input_file_path,"r");
	output_file = open(output_file_path,"w");
	
	test_count  = int(input_file.readline());
	
	for index in xrange(test_count):
	  test_case = [ int(x) for x in input_file.readline().split()]
	  
	  n,s,p,t = test_case[0],test_case[1],test_case[2],test_case[3:];	  	  
	  best_danceer_count = get_best_dancer_count(s,p,t);
	  solution_string = "Case #%d: %d"%(index+1,best_danceer_count);			
	  print solution_string;
	  output_file.write(solution_string+'\n');
	
	input_file.close()
	output_file.close()

	
def  start_me_up():
	if len(sys.argv) == 1:
		print "Usage:"
		print "%s input_file_path [output_file_path]" % ( sys.argv[0]);		
		print "Note: Solution is output to console too." ;		

	elif len(sys.argv) == 2:
		solve_problem(sys.argv[1], sys.argv[1]+'.out');
	
	elif len(sys.argv) >= 3:	
		solve_problem(sys.argv[1], sys.argv[2]);
		


if __name__ == "__main__":
	start_me_up();


