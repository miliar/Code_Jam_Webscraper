#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>

using namespace std;


int main()
{	
	ifstream input_file;
	input_file.open("A-small-attempt11.in");

	if( !input_file.is_open() ) {
		cout << "The file is not open!\n";
	}

	vector<string> whole_data;

	string str;
	char buffer[256];
	while( !input_file.eof() ) {
		input_file.getline(buffer,sizeof(buffer));
		str = buffer;
		whole_data.push_back(str);
	}

	input_file.close();

	vector<string> data;
	vector< vector<string> > search_engine_data;
	vector< vector<string> > query_data;

	int problem_size = 0;
	int counter = 0;
	int loop_counter;

	problem_size = atoi( whole_data[counter].c_str() );
	++counter;
	for(int j=0; j!=problem_size; ++j ) {
		loop_counter = atoi( whole_data[counter].c_str() );
		++counter;
		//cout << loop_counter << endl;
		for(int i=0; i!=loop_counter; ++i ) {
			data.push_back( whole_data[counter] );
			++counter;
			}
		search_engine_data.push_back(data);
		data.clear();
		loop_counter = atoi( whole_data[counter].c_str() );
		++counter;
		//cout << loop_counter << endl;
		for(int i=0; i!=loop_counter; ++i ) {
			data.push_back( whole_data[counter] );
			++counter;
			}
		query_data.push_back(data);
		data.clear();
	}

	//////////////////////////////////////////////////////////////////////

	ofstream ofs( "output_true.txt" );
	int sum = 0;

	for(int j=0; j!=problem_size; ++j ) {
		vector<int> problem;
		problem.clear();
		map<string,int> search_engine_list;
		for(int i=0; i!=search_engine_data[j].size(); ++i ) {
			search_engine_list.insert( pair<string,int>(search_engine_data[j][i],i) );
		}
		for(int i=0; i!=query_data[j].size(); ++i ) {
			map<string,int>::iterator map_ite;
			map_ite = search_engine_list.find(query_data[j][i]);
			problem.push_back( (int)(*map_ite).second );
		}
		//cout << search_engine_list.size() << " " << problem.size() << endl;


		pair<int,int> before_best_position_cost = pair<int,int>(0,0);
		pair<int,int> current_best_position_cost = pair<int,int>(0,0);

		int current_engine;
		while( current_best_position_cost.first != problem.size() ) {
			bool end_flag = false;
			map<string,int>::iterator map_ite;
			for( map_ite = search_engine_list.begin(); map_ite!=search_engine_list.end(); ++map_ite ) {
				current_engine = (*map_ite).second;
				pair<int,int> position_cost = before_best_position_cost;
				bool flag = false;
				while( position_cost.first != problem.size() ) {
					if( current_engine==problem[position_cost.first] ) {
						++position_cost.second;
						flag = true;
						break;
					}
					++position_cost.first;
				}
				//cout << position_cost.first << endl;
				/*
				if(flag) {
					++position_cost.second;
				}
				*/
				if( current_best_position_cost.first < position_cost.first ) {
					 current_best_position_cost = position_cost;
				}
			}
			before_best_position_cost = current_best_position_cost;
		}

		cout << "Case #" << j+1 << ": " << current_best_position_cost.second << endl;
	}

	ofs.close();

	return 0;
}