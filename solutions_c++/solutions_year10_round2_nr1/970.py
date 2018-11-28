#include <cstdio>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <iterator>
#include <set>
using namespace std;
#include <boost/algorithm/string.hpp>
#include <boost/foreach.hpp>

typedef vector<string> VS;
int T, N, M;
VS e;
VS ne;

int solve()
{
	set<string> exists;
	for( int i = 0; i < e.size(); ++i )
	{
		VS tokens;
		boost::split( tokens, e[i], boost::is_any_of("/") );

		string path;
		for( int j = 0; j < tokens.size(); ++j )
		{
			if ( ! tokens[j].empty() )
			{
				path += "/" + tokens[j];
				exists.insert( path );
			}
		}
	}
	int result = 0;
	for( int i = 0; i < ne.size(); ++i )
	{
		VS tokens;
		boost::split( tokens, ne[i], boost::is_any_of("/") );

		string path;
		for( int j = 0; j < tokens.size(); ++j )
		{
			if ( ! tokens[j].empty() )
			{
				path += "/" + tokens[j];
				if ( exists.find(path) == exists.end() )
				{
					++result;
					exists.insert( path );
				}
			}
		}
	}
	//BOOST_FOREACH( string const& s, exists )
	//	cout << s << endl;
	return result;
}

int main()
{
	freopen( "A-large.in", "rt", stdin );
	freopen( "A-large.in.out", "wt", stdout );

	scanf( "%d", &T );
//	printf( "%d\n", T );
	for( int n = 0; n < T; ++n )
	{
		e.clear(); ne.clear();
		scanf( "%d %d\n", &N, &M );
		for( int i = 0; i < N; ++i )
		{
			std::string buffer;
			std::getline(std::cin, buffer);
			e.push_back(buffer);
		}

		for( int i = 0; i < M; ++i )
		{
			std::string buffer;
			std::getline(std::cin, buffer);
			ne.push_back(buffer);
		}

//		printf("%d %d\n", N, M);
//		for( int i = 0; i < N; ++i )
//			printf( "%s\n", e[i].c_str() );
//		for( int i = 0; i < M; ++i )
//			printf( "%s\n", ne[i].c_str() );

		printf( "Case #%d: %d\n", n + 1, solve() );
	}
}
