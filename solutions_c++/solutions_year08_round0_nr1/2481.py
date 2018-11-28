#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;

/* "Saving The Universe" Solution: C. Cunningham, chris.r.cunningham@gmail.com */

int main (int argc, char * const argv[]) {
	
	ifstream input_file; 
	string line;
	string *search_engine_list, *searches; 
	unsigned int cases, case_count, i, j, search_engines_seen_count,\
		total_count, num_search_engines, num_searches, num_switches;
	ostringstream stm; 	
	bool *search_engines_seen;
	
	
	input_file.open(argv[1]);
	
	if(!input_file.is_open()){
		cout << "Input file not found" << endl;
		return -1;
	}
	
	
	getline(input_file, line);	
	cases = atoi(line.c_str());	
	
	case_count = 1;
	while(case_count <= cases){			
		cout << "Case #" << case_count++ << ": ";
		
		/** Process Current Case **/
		
		/* Get the number of search engines */
		getline(input_file, line); 
		num_search_engines = atoi(line.c_str());
		search_engine_list = new string[num_search_engines];
		
		/* Get search engine list */
		for(i=0; i<num_search_engines; i++){ 
			getline(input_file, search_engine_list[i]);
		}
		
		/* Get the number of searches */
		getline(input_file, line); 
		num_searches = atoi(line.c_str());
		searches = new string[num_searches];
		
		/* Get search list*/
		for(i=0; i<num_searches; i++){ 
			getline(input_file, searches[i]);
		}
		
		
		
		/* Process string matrices to speed up searching */
		for(i=0; i<num_search_engines; i++){
			for(j=0; j<num_searches; j++){
				if(searches[j] == search_engine_list[i]){
					stm << i; 
					searches[j] = stm.str();
					stm.str("");
				}
			}
		}
		
		
		search_engines_seen = new bool[num_search_engines];
		num_switches = 0;
		total_count = 0;
		
		/* Loop through all of the searches */
		for(;;){			
			search_engines_seen_count = 0;			
			for(j=0; j<num_search_engines; j++)
				search_engines_seen[j] = false;
			
			
			/* Move through the list until we need to make a switch */
			while(search_engines_seen_count < num_search_engines){		
				/* Check if we are done */
				if(total_count == num_searches){
					break;
				}				
				/* Check if this search engine has already been seen */
				if(search_engines_seen[atoi(searches[total_count].c_str())] == false){
					search_engines_seen[atoi(searches[total_count].c_str())] = true;
					search_engines_seen_count++;
				}
				total_count++; /* Increment the number of searches that we have processed */			
				
			}
			if(total_count == num_searches){
				if(search_engines_seen_count == num_search_engines){  /* Case where we have to switch on the last search */
					num_switches++;
					break;
				}else{ /* Done! */
					break;
				}
			}
			else{
				num_switches++; /* Perform a switch */
				total_count--; /* Make sure we consider the search engine that was last used */
			}
				
		}	
		cout << num_switches <<endl; /* Result */
		/* Free up some memory */
		delete[] search_engines_seen; 
		delete[] search_engine_list;
		delete[] searches;
	}
	/* Close output file */
	input_file.close();
    return 0;
}









