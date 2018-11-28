// recycled.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <vector>
#include <utility>
#include <string>
#include <iterator>
#include <algorithm>
#include <iostream>
#include <cmath>
using namespace std;

#include <boost/tokenizer.hpp>
#include <boost/lexical_cast.hpp>

using namespace boost;

void read_pairs( string const & filename, vector<pair<int,int>> & pairs )
{
	ifstream ifs(filename);
	string s;
	getline( ifs, s );
	int n = lexical_cast<int>(s);

	pairs.reserve(n);
	for ( int i = 0; i < n; ++i )
	{
		getline(ifs, s );
		tokenizer<> tok(s);
		tokenizer<>::iterator t = tok.begin();
		int a = lexical_cast<int>( *t );
		int b = lexical_cast<int>( *(++t) );
		pairs.push_back( make_pair( a, b ) );
	}
}

int count_recycled_numbers( int a, int b )
{
	// determine number of digits
	int ndigits = static_cast<int>( log10( (double) a) ) + 1;
	if ( ndigits == 1 )
	{
		return 0;
	}
	int sum = 0;
	// for each potential value of n
	vector<pair<int,int> > candidates;
	for ( int n = a; n <= b; ++n )
	{
		// for each potential number of digits
		for ( int d = 1; d < ndigits; ++d )
		{
			int divisor = static_cast<int>( pow(10.0,d) );
			int lower = n % divisor;
			if ( lower == 0 )
			{
				continue;
			}
			int higher = n / divisor;
			int mul = static_cast<int>( pow( 10.0, ndigits - d ) );
			int m = lower * mul + higher;
			if ( m > n && m <= b )
			{
				candidates.push_back( make_pair(n,m) );
			}
		}
		
	}
	vector<pair<int,int>>::iterator end = unique( candidates.begin(), candidates.end(), 
		[]( pair<int,int> a, pair<int,int> b ) { return a.first==b.first && a.second==b.second; } );
	return distance(candidates.begin(), end );
}

int main(int argc, char * argv[] )
{
	vector<pair<int,int> > pairs;
	read_pairs( argv[1],  pairs );

	int n = pairs.size();
	for ( int i = 0; i < n; ++i )
	{
		int count = count_recycled_numbers( pairs[i].first, pairs[i].second ) ;
		cout << "Case #" << i+1 << ": " << count << "\n";
	}
}

