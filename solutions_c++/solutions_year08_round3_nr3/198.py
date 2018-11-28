#include<cstdio>
#include<iostream>
#include<vector>
#include<set>
#include<queue>
#include<algorithm>
#include<cmath>

using namespace std;

int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int t;
	cin >> t;
	for( int test = 1; test <= t; ++test )
	{
		cout << "Case #" << test << ": ";	
		int n, m, x, y, z;
		cin >> n >> m >> x >> y >> z;
		vector<int>v1( m );
		for( int i = 0; i < m; ++i )
			cin >> v1[ i ];
		vector<int> v( n );
		for( int i = 0; i < n; ++i )
		{
			v[ i ] = v1[ i % m ];
			long long X = x, Y = y, Z = z, I = i + 1, A = v1[ i % m ];
			long long res = ( X * A + Y * I ) % Z;
			v1[ i % m ] = res;
		}
		vector<long long> f( n );
		long long res = 0;
		f[ 0 ] = 0;
		for( int i = 0; i < n; ++i ) 
		{
			for( int j = 0; j < i; ++j )
				if( v[ i ] > v[ j ] )
				{
					f[ i ] += f[ j ];
					f[ i ] %= 1000000007;
				}
			++f[ i ];
			f[ i ] %= 1000000007;
			res += f[ i ];
			res %= 1000000007;
		}
		cout << res << endl;

	}
	return 0;
}