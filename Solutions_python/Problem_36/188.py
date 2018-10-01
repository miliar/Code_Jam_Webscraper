
import sys
import string


class Indexed:
	def __init__(self, seq):
		self.seq = seq;
	def __getitem__(self, i):
		return self.seq[i], i;

def find_index(search_character, text ,start_index):
	for character, index in Indexed(text[start_index:]):
		if character ==  search_character:
			return  index + start_index;
	return None;	

solution_memo ={};

def search( search_string , text ):
	
	#check stored solutions
	global solution_memo;
	if solution_memo.has_key( (search_string , text)):
		return solution_memo[(search_string , text)];
	
	search_count = 0;
	search_character = search_string[0];
	text_len =  len(text);
	text_index = 0;

	while True: 
		if text_index >= text_len:
			break;	
		found_index = find_index(search_character, text , text_index );
		if found_index is not None:
			
			text_index = found_index +1;
			if len(search_string) == 1 :
				search_count+=1;
			else:	
				search_count+=search( search_string[1:] , text[found_index:]);	
		else:
			break;
	
	# store solution	
	solution_memo[(search_string , text)] = search_count ;
	return search_count;


def find_subsequence_count(text):
	count = search("welcome to code jam",text);
	count_string = ("%04d")%(count);
	return count_string[-4:];

def solve_welcome_to_code_jam_problem(input_file_path , output_file_path):
		
	input_file = open(input_file_path,"r");
	output_file = open(output_file_path,"w");
	
	count_test_cases  = int(input_file.readline());
	
	for index in xrange(count_test_cases):
		solution_string = "Case #%d: %s"%(index+1,find_subsequence_count(input_file.readline()));			
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
		solve_welcome_to_code_jam_problem(sys.argv[1], sys.argv[1]+'.out');
	
	elif len(sys.argv) >= 3:	
		solve_welcome_to_code_jam_problem(sys.argv[1], sys.argv[2]);
		


if __name__ == "__main__":
	start_me_up();














