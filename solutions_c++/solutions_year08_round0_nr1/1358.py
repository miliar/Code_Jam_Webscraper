#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int main() 
{
	/* Start by opening the input file */
	ifstream infile( "A-large.in" );
	
	/* Prepare output file stream */
	ofstream outfile( "output.txt" );

	/* Line 1: Aquire number of test cases */
	int num_of_cases;
	infile >> num_of_cases;

	for( int i = 0; i != num_of_cases; ++i ) {
		
		/* Get number of search engines */
		int num_of_engines;
		infile >> num_of_engines;
		infile.get();

		/* Name of each search engine */
		vector<string> engine_names;
		for(int j = 0; j != num_of_engines; ++j ) {
			string name;
			getline(infile, name);
			engine_names.push_back(name);
		}
		
		int num_of_queries;
		infile >> num_of_queries;
		infile.get();

		/* Record of queries */
		vector<string> query_list;
		for( int j = 0; j != num_of_queries; ++j ) {
			string query;
			getline(infile, query);
			query_list.push_back( query);
		}

		vector<string>::iterator current_iter = query_list.begin();
		string best_engine;
		int num_of_switch = num_of_queries>0?-1:0;
		
		
		

		while( current_iter != query_list.end() ) {
				

			vector<string>::iterator iter = current_iter;
			for( int j = 0; j != engine_names.size(); ++j ) {
				vector<string>::iterator result = find( iter, query_list.end(), engine_names[j]);
				if( result > current_iter ) {
					best_engine = engine_names[j];
					current_iter = result;
				}
			}
			num_of_switch++;
			
		}

		outfile << "Case #" << i+1 << ": " << num_of_switch << endl;
		cout << "Case #" << i+1 << ": " << num_of_switch << endl;
	}
	
	infile.close();
	outfile.close();

	system("pause");
	return 0;
}
