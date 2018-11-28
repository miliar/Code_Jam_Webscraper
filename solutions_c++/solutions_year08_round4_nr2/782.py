#include<cstdio>
#include<iostream>
#include<vector>
#include<set>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>

using namespace std;

#define P pair<int,int>

int getS( P a, P b, P c )
{
	return ( a.second + b.second ) * ( b.first - a.first ) +
		( b.second + c.second ) * ( c.first - b.first ) + 
		( a.second + c.second ) * ( a.first - c.first );
}
int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int t;
	cin >> t;
	for( int test = 1; test <= t; ++test )
	{
		printf( "Case #%d: ", test );
		int n, m, A;
		cin >> n >> m >> A;
		pair<int,int> zero;
		pair<int,int> a, b;
		zero = make_pair( 0, 0 );
		for( int x1 = 0; x1 <= n; ++x1 )
		{
			for( int y1 = 0; y1 <= m; ++y1 )
				for( int x2 = 0; x2 <= n; ++x2 )
					for( int y2 = 0; y2 <= m; ++y2 )
					{
						
						a = make_pair( x1, y1 );
						b = make_pair( x2, y2 );
						int sq = getS( a, b, zero );
						if( sq == A )
							goto lab;
					}
		}
		cout << "IMPOSSIBLE\n";
		continue;
lab:	
		printf( "%d %d %d %d %d %d\n", zero.first, zero.second, a.first, a.second, b.first, b.second );
			
	}
	return 0;
}