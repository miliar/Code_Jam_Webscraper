/*
 * 2008. Gooogle Code Jam.
 * Qualification Round
 *   A. Saving the Universe
 * Code by Kyoungmoon Sun
 */

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

class CentralSystem
{
private:
	vector<string> queries;
	map<string, int> engines;

public:
	void addQuery( string query )
	{
		// continous same query? skip it!
		if( queries.size() > 0 && queries.back() == query )
			return;
		queries.push_back( query );
	}

	void addEngine( string engine )
	{
		engines[engine] = 0;
	}

	int send()
	{
		vector<string>::reverse_iterator qitr;
		vector<string>::reverse_iterator prev_qitr;
		map<string, int>::iterator eitr;
		int min = INT_MAX;

		for( qitr = queries.rbegin(); qitr != queries.rend(); qitr++ )
		{
			min = INT_MAX;
			if( qitr != queries.rbegin() )
			{
				for( eitr = engines.begin(); eitr != engines.end(); eitr++ )
				{
					if( eitr->second >= 0 && min > eitr->second )
						min = eitr->second;
				}
				engines[*prev_qitr] = min + 1;
			}
			engines[*qitr] = -1;
			prev_qitr = qitr;
		}

		min = INT_MAX;
		for( eitr = engines.begin(); eitr != engines.end(); eitr++ )
		{
			if( eitr->second >= 0 && min > eitr->second )
				min = eitr->second;
		}

		return min;
	}
};

int str2int( string str )
{
	stringstream stream( str );
	int result;
	stream >> result;
	return result;
}

void process( char* filename )
{
	int caseCount, queryCount, engineCount;
	int i, j;
	string str;

	ifstream inputfile( filename );

	if( !inputfile.is_open() )
	{
		cout << "Unable to open " << filename << endl;
		return;
	}

	getline( inputfile, str );
	caseCount = str2int( str );

	for( i = 0; i < caseCount; i++ )
	{
		CentralSystem system;
		int result;

		getline( inputfile, str );
		engineCount = str2int( str );

		for( j = 0; j < engineCount; j++ )
		{
			string engine;
			
			getline( inputfile, engine );
			inputfile.clear();
			system.addEngine( engine );
		}

		getline( inputfile, str );
		queryCount = str2int( str );

		for( j = 0; j < queryCount; j++ )
		{
			string query;

			getline( inputfile, query );
			inputfile.clear();
			system.addQuery( query );
		}

		result = system.send();
		cout << "Case #" << i + 1 << ": " << result << endl;
	}

	inputfile.close();
}

int main( int argc, char* argv[] )
{
	if( argc != 2 )
	{
		cout << argv[0] << " [input file]" << endl;
		return 0;
	}

	process( argv[1] );

	return 0;
}
