#include<iostream>

using namespace std;
const int MAXN = 1111;

int a[ MAXN ];

int main()
{
	freopen( "input.txt","rt", stdin );
	freopen( "output.txt","wt", stdout );
	int tests;
	cin >> tests;
	for( int t = 1; t <= tests; t++ )
		{
			int n;
			cin >> n;
			int sum = 0;
			for( int i = 0; i < n; i++ )
			{
				cin >> a[ i ];
				sum += a[ i ];
			}
			int res = -1;
			for( int i = 0; i < n; i++ )
				{
					int cur = 0;
					for( int j = 0; j < n; j++ )
						if( i != j )
							cur ^= a[ j ];
					if( cur == a[ i ] )
						res = max( res, max( a[ i ], sum - a[ i ]) );
				}
			cout << "Case #" << t << ": ";
			if( res == -1 )
				cout << "NO" << endl;
			else
				cout << res << endl;
		}

}