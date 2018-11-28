#include <iostream>
#include <string>
#include <map>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main(int argc, char* argv[])
{
	int no_of_test_case = 0;
	string s_no_of_test_case;

	getline(cin, s_no_of_test_case, '\n');
	no_of_test_case = atoi(s_no_of_test_case.c_str());

	map<string, bool> search_engines;
	string name_of_search_engine;
	string query;

	for(int i = 1; i <= no_of_test_case; ++i)
	{
		int no_of_search_engine = 0;
		string s_no_of_search_engine;
		
		getline(cin, s_no_of_search_engine, '\n');
		no_of_search_engine = atoi(s_no_of_search_engine.c_str());

		search_engines.clear();
		
		for(int j = 0; j < no_of_search_engine; ++j)
		{
			getline(cin, name_of_search_engine, '\n');
			search_engines[name_of_search_engine] = false;
		}

		int no_of_query = 0;
		string s_no_of_query;
		
		getline(cin, s_no_of_query, '\n');
		no_of_query = atoi(s_no_of_query.c_str());

		int no_of_failed = 0;
		int no_of_switch = 0;

		for(int k = 0; k < no_of_query; ++k)
		{
			getline(cin, query, '\n');

			if(search_engines[query] == true)
				continue;
			else
			{
				search_engines[query] = true;
				++no_of_failed;
				
				if(no_of_failed == no_of_search_engine)
				{
					++no_of_switch;
					no_of_failed = 1;
					map<string, bool>::iterator it;
					for(it = search_engines.begin(); it != search_engines.end(); ++it)
						it->second = false;
				}
				search_engines[query] = true;
			}
		}
		cout << "Case #" << i << ": " << no_of_switch << endl;
	}
	return 0;
}
