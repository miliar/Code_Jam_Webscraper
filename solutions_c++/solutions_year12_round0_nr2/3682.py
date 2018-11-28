#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <fstream>
#include <ostream>
#include <sstream>
#include <assert.h>
using namespace std;

bool possible( int a, int b, int c )
{
	return abs( a - b ) <= 2 && abs( a - c ) <= 2 && abs( b - c ) <= 2;
}

int surp( int a, int b, int c )
{
	return abs( a -b ) > 1 || abs( a - c ) > 1 || abs( b -c ) > 1;
}

int main(int argc, char* argv[ ] )
{
	freopen( "in.txt", "rt", stdin );
	freopen( "out.txt", "wt", stdout );

	int T = 0;
	cin >> T;
	for ( int ct = 1; ct <= T; ++ct )
	{
		vector<int> total;
		int n = 0, s = 0, p = 0;
		cin >> n >> s >> p;
		for( int i = 0; i < n; ++i )
		{
			int k;
			cin >> k;
			total.push_back( k );
		}
		vector<pair<int,int> > wins( n );

		int totalSurpOnly = 0;
		int totalSureAndSurp = 0;
		int totalSureOnly = 0;

		for( int i = 0; i < total.size( ); ++i )
		{
			for( int a = 0; a <= 10; ++a )
			{
				for( int b = 0; b <= 10; ++b )
				{
					for( int c = 0; c <= 10; ++c )
					{
						if( a + b + c == total[ i ] && max( a, max( b,c )  ) >= p )
						{
							if( possible( a, b, c ) )
							{
								wins[ i ].first++;
							}

							if( possible( a, b, c )&& surp( a, b, c ) )
							{
								wins[ i ].second++;
							}
						}

					}
				}
			}

			if( wins[ i ].first > 0 && wins[ i ].second > 0 && wins[ i ].first == wins[ i ].second )
			{
				totalSurpOnly++;
			}
			else if( wins[ i ].first > 0 && wins[ i ].second > 0 && wins[ i ].first > wins[ i ].second )
			{
				totalSureAndSurp++;
			}
			else if( wins[ i ].first > 0 && wins[ i ].second == 0 )
			{
				totalSureOnly++;
			}
			else if( wins[ i ].first == wins[ i ].second && wins[ i ].first == 0 )
			{

			}
			else
			{
				assert( false );
			}
		}

		int res = totalSureAndSurp + totalSureOnly;
		res += min( s, totalSurpOnly );
		cout << "Case #" << ct << ": " << res << endl;
	}

}