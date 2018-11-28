// Saving The World.cpp : Defines the entry point for the console application.
//

#include <string>
#include <vector>

#include <iostream>

typedef std::vector<std::string> array_string;

using std::string;

using std::cin;
using std::cout;

long count_minimum_switchs(const array_string& search_engines, const array_string& queries);


int main(int argc, char* argv[])
{
	unsigned long total_cases;         // Total of cases to be tested

	unsigned long total_search_engines;// Total of search engine 
	unsigned long total_queries;       // Total of queries

	string search_engine_name;         // Name of search engine (eg. Googol)
	string query;					   // The query to search engine

	array_string search_engines;       // Array of search engines names
	array_string queries;              // Array of queries strings

	cin >> total_cases;

	cin.ignore();
	cin.clear();

	for(unsigned long i = 1; i <= total_cases; i++)
	{
		cin >> total_search_engines;
		cin.ignore();
		cin.clear();

		search_engines.clear();
		queries.clear();
		
		for(unsigned long j = 0; j < total_search_engines; j++)
		{
			std::getline(cin,search_engine_name);
			search_engines.push_back(search_engine_name);
		}

		cin >> total_queries;
		cin.ignore();
		cin.clear();

		for(unsigned long k = 0; k < total_queries; k++)
		{
			std::getline(cin,query);
			queries.push_back(query);
		}

		long total_switchs = count_minimum_switchs(search_engines, queries);
		
		cout << "Case #" << i <<": " << total_switchs << std::endl;
	}
	return 0;
}

long count_minimum_switchs(const array_string& search_engines, const array_string& queries)
{
	if(search_engines.empty())
		return 0;

	if(queries.empty())
		return 0;

	long total_switch = 0;

	array_string::const_iterator it_engines; // iteretor of search engines
	array_string::const_iterator it_queries; // iterator of queries

	array_string::const_iterator it_queries_base; // base iterator to queries
	array_string::const_iterator it_queries_last; // last iterator to greater difference

	it_queries_base = queries.begin();

	do
	{
		it_queries_last = it_queries_base;

		for(it_engines = search_engines.begin(); it_engines != search_engines.end() && it_queries_last != queries.end(); it_engines++)
		{
			const string & search_engine = *it_engines;
			
			it_queries = it_queries_base;

			while(it_queries != queries.end())
			{
				const string & query = *it_queries;
				if(search_engine == query)
				{
					if(it_queries > it_queries_last)
						it_queries_last = it_queries;
					break;
				}
				it_queries++;
			}
			if(it_queries == queries.end())
				it_queries_last = queries.end();
		}
		if(it_queries_last != it_queries_base && it_queries_last != queries.end())
		{
			it_queries_base = it_queries_last;
			total_switch ++;
		}
	} while(it_queries_last != queries.end());

	return total_switch;
}

