#include <iostream>
#include <fstream>
#include <vector>
#include <map>

#define MAX_SIZE 1005

using namespace std;

struct strCmp {
	bool operator()( const char* s1, const char* s2 ) const {
      return strcmp( s1, s2 ) < 0;
    }
};

void reset(std::map<char*, int, strCmp> &search_term_counter);

void main()
{
	std::ifstream input_file ("C:\\Temp\\A-large.in");
	std::ofstream  output_file("C:\\Temp\\output_large.out");
	
	if(input_file.is_open())
	{
		int case_count;
		input_file  >> case_count;
		for(int i=0; i<case_count; i++)
		{
			char **search_engines;
			std::map<char*, int, strCmp> search_term_counter;  
			int flag_counter = 0;
			int no_of_switches = 0;
			int search_engine_count, query_count;
			input_file >> search_engine_count;
			search_engines = new char*[search_engine_count];
			

			//form an array of search engine names for further reference
			// and initialize their mapping entries
			for(int j=0; j<search_engine_count; j++)
			{
				search_engines[j] = new char[MAX_SIZE];
				input_file.getline(search_engines[j], MAX_SIZE);
				if((j==0) && (!strcmp(search_engines[0],"")))
					input_file.getline(search_engines[0], MAX_SIZE);
				search_term_counter[search_engines[j]] = 0;
			}
					
			input_file >> query_count;
			char old_query[MAX_SIZE] = "";
			for(int k =0; k < query_count; k++)
			{
				char query[MAX_SIZE] = "";	
				input_file.getline(query, MAX_SIZE);
				if((k==0) && (!strcmp(query,"")))
					input_file.getline(query, MAX_SIZE);
				
				if(strcmp(query, old_query) != 0)
				{
					if(search_term_counter[query] == 0)
					{
						search_term_counter[query] = 1;
						flag_counter++;
						if(flag_counter == search_engine_count)
						{
							no_of_switches++;
							reset(search_term_counter);
							flag_counter = 1;
							search_term_counter[query] = 1;
						}
					}
					strcpy(old_query, query);
				}
			}

			output_file << "Case #" << (i+1) << ": " << no_of_switches << "\n" ;
		}
		input_file.close();
		output_file.close();
	}
	
}

void reset(std::map<char*, int, strCmp> &search_term_counter)
{
	std::map<char*, int, strCmp>::iterator map_iter;
	for(map_iter = search_term_counter.begin();
		map_iter != search_term_counter.end(); ++map_iter)
	{
		map_iter->second = 0;
	}
}
