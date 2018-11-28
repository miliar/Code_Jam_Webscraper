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
		int p, k, l;
		cin >> p >> k >> l;
		vector<pair<long long,int> > v( l );
		for( int i = 0; i < l; ++i )
		{
			int a;
			cin >> a;
			v[ i ] = make_pair( a, i );
		}
		sort( v.begin(), v.end() );
		long long res = 0;
		int cur = 0;
		long long c = 1;
		for( int i = l - 1; i >= 0; --i )
		{
			res += ( c * v[ i ].first );
			++cur;
			if( cur >= k )
			{
				++c;
				cur = 0;
			}
		}
		cout << res << endl;
	}
	return 0;
}