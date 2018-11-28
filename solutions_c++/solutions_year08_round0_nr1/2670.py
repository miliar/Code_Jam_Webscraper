#include <iostream>
#include <cassert>
#include <stdexcept>
#include <limits>

#include <vector>
#include <string>
#include <map>
#include <list>
#include <sstream>

typedef std::vector< std::string > Queries;
typedef std::vector< std::string > SearchEngines;
typedef std::map< Queries::iterator, int > JumpsCache;

int current_minimum;
SearchEngines engines;
Queries queries;
JumpsCache cache;

class Test
{
public:
	Test( int j, Queries::iterator q, std::string e );
	void process( );
	void change_engine( );

private:
	int jumps;
	Queries::iterator queue;
	std::string engine;
};

typedef std::list< Test > Tests;
Tests tests;
	
Test::Test( int j, Queries::iterator q, std::string e ):
	jumps( j ), queue( q ), engine( e )
{
}

void Test::process( )
{
	while ( queue != queries.end() && *queue != engine )
	{
		if ( jumps >= current_minimum || jumps-1 >= cache[queue] )
		{
			return;
		}
		if ( jumps < cache[queue] )
		{
			cache[queue] = jumps;
		}
		++queue;
	}
	if ( queue == queries.end( ) )
	{
		if ( jumps < current_minimum )
		{
			current_minimum = jumps;
		}
	}
	else
	{
		++queue;
		change_engine( );
	}
}

void Test::change_engine( )
{
	if ( jumps+1 >= current_minimum )
	{
		return;
	}

	for ( SearchEngines::iterator it = engines.begin(); it != engines.end(); ++it )
	{
		if ( *it == engine )
		{
			continue;
		}

		tests.push_back( Test(jumps+1, queue, *it) );
	}
}

int main( )
{
	int n;
	{
		std::string line;
		std::getline( std::cin, line );
		std::stringstream ss( line );

		ss >> n;
	}

	for ( int test = 0; test < n; ++test )
	{
		int s, q;
		tests.clear( );
		cache.clear( );
		current_minimum = std::numeric_limits<int>::max( );
		
		engines.clear( );
		{
			std::string line;
			std::getline( std::cin, line );
			std::stringstream ss( line );

			ss >> s;
		}
		for ( int i = 0; i < s; ++i )
		{
			std::string engine;
			std::getline( std::cin, engine );
			engines.push_back( engine );
		}
		
		queries.clear( );
		{
			std::string line;
			std::getline( std::cin, line );
			std::stringstream ss( line );

			ss >> q;
		}
		for ( int i = 0; i < q; ++i )
		{
			std::string query;
			std::getline( std::cin, query );
			queries.push_back( query );
		}
		for ( Queries::iterator it = queries.begin(); it != queries.end(); ++it )
		{
			cache[it] = current_minimum;
		}
		cache[queries.end()] = current_minimum;

		Test( -1, queries.begin( ), "" ).change_engine( );
		while ( !tests.empty() )
		{
			Test current = tests.back( );
			tests.pop_back( );
			current.process( );
		}

		std::cout << "Case #" << test+1 << ": " << current_minimum << std::endl;
	}

	return 0;
}
