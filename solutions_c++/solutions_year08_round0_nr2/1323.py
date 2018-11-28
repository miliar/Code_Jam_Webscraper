#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <functional>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <queue>
#include <vector>
using namespace std;
typedef vector<int> vi;
#define fora(i,v) for(int i = 0; i < (v).size(); i++)
template<typename T, typename Predicate> vector<T> Parse( string s, Predicate predicate )
{
	vector<T> result; bool isWord = false; int j = 0;
	for( int i = 0; i < s.size(); i++ )
		if ( isWord )
		{
			if ( !predicate( s[i] ) )
			{
				istringstream S( s.substr( j, i - j ) );
				T current; S >> current; 
				if ( S.rdstate() ^ ios::failbit )
					result.push_back( current );
				isWord = false;
			}
		}
		else
		{
			if ( predicate( s[i] ) )
			{
				j = i; isWord = true;
			}
		}
	if ( isWord )
	{
		istringstream S( s.substr( j ) );
		T current; S >> current; 
		if ( S.rdstate() ^ ios::failbit )
			result.push_back( current );
	}
	return result;
}
struct split_helper: unary_function<int, bool>
{
	explicit split_helper( string delimeter ): delimeter(delimeter) {};
	bool operator() ( int c ) const
	{
		return delimeter.find( c ) == string::npos;
	}
private: string delimeter;
};
template <typename T> vector<T> Split( string s, string delimeter = " " )
{
	return Parse<T>( s, split_helper( delimeter ) );
}
int parse_time( const string& s )
{
    vi z( Split<int>( s, ":" ) );
    return z[0] * 60 + z[1];
}
int main()
{
    ifstream input( "test.in" );
    ofstream output( "test.out" );
    int N; input >> N;
    for( int n = 0; n < N; ++n )
    {
        int resultA = 0, resultB = 0;
        int T; input >> T;
        int NA, NB; input >> NA >> NB;
        vi A1, A2, B1, B2;
        for( int na = 0; na < NA; ++na )
        {
            string a, b;
            input >> a >> b;
            A1.push_back( parse_time( a ) ); A2.push_back( parse_time( b ) + T );
        }
        for( int nb = 0; nb < NB; ++nb )
        {
            string a, b;
            input >> a >> b;
            B1.push_back( parse_time( a ) ); B2.push_back( parse_time( b ) + T );
        }
        int x = 0, y = 0;
        for( int time = 0; time < 24 * 60; ++time )
        {
            fora(i, A2)
                if ( A2[i] == time )
                    ++y;
            fora(i, B2)
                if ( B2[i] == time )
                    ++x;
            fora(i, A1)
                if ( A1[i] == time )
                {
                    if ( x )
                        --x;
                    else
                        ++resultA;
                }
            fora(i, B1)
                if ( B1[i] == time )
                {
                    if ( y )
                        --y;
                    else
                        ++resultB;
                }
        }
        output << "Case #" << n + 1 << ": " << resultA << " " << resultB << endl;
    }        
    return 0;
}