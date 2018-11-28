#include <iostream>
#include <string>
#include <vector>
#include <map>

#define CASE_MAX_NUM			20
#define SEARCH_ENGINE_MAX_NUM	100
#define QUERY_MAX_NUM			1000

using namespace std;

#ifdef __DEBUG__
void PrintEngine( const map<string, int> & m )
{
	map<string, int>::const_iterator iter = m.begin();
	while ( iter != m.end() )
	{
		cout << iter->first << ":" << iter->second << endl;
		iter++;
	}

}

void PrintQuery( const vector<string> & v )
{
	vector<string>::const_iterator iter = v.begin();
	while ( iter != v.end() )
	{
		cout << *iter << endl;
		iter++;
	}
}
#endif

void ReadEngine( int & n, map<string, int> & m )
{
	cin >> n;
	cin.get();

	string s;

	for ( int i = 0 ; i < n ; ++i )
	{
		getline( cin, s );
		m[ s ] = i;	
	}
}

void ReadQuery( int & n, vector<string> & v )
{
	cin >> n;
	cin.get();

	string s;

	for ( int i = 0 ; i < n ; ++i )
	{
		getline( cin, s );
		v.push_back( s );
	}
}

int RunQuery(
	const vector<string> & query,
	map<string, int> & engine )
{
	int nSwitch = 0;

	char engineMask[ SEARCH_ENGINE_MAX_NUM ] = { 0 };
	int nRemain = engine.size();
	memset( engineMask, 0x1, nRemain * sizeof (char) );

	vector<string>::const_iterator iter = query.begin();

	while ( iter != query.end() )
	{
		int engineId = engine[ *iter ];
		if ( engineMask[engineId] & 1 )
		{
			if ( nRemain - 1 == 0 )
			{
				++nSwitch;
				nRemain = engine.size();
				memset( engineMask, 0x1, nRemain * sizeof (char) );
			}

			--nRemain;
			engineMask[engineId] = 0;
		}

		iter++;
	}

	return nSwitch;
}

inline void PrintResult( int caseId, int nSwitch )
{
	cout << "Case #" << caseId << ": " << nSwitch << endl;
}

int main()
{
	int nCase;
	int nEngine;
	int nQuery;

	map<string, int> engine;
	vector<string> query;

	query.reserve( QUERY_MAX_NUM );

	cin >> nCase;

	for ( int i = 0 ; i < nCase ; ++i )
	{
		ReadEngine( nEngine, engine );
		ReadQuery( nQuery, query );

#ifdef __DEBUG__
		PrintEngine( engine );
		PrintQuery( query );
#endif
		PrintResult( i + 1, RunQuery( query, engine ) );

		engine.clear();
		query.clear();
	}

	return 0;
}

