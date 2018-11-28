#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <string>
#include <map>
#include <algorithm>
#include <functional>
#include <numeric>
using namespace std;


int main( )
{
	freopen( "input.txt", "rt", stdin );
	freopen( "output.txt", "wt", stdout );	

	int T = 0;
	cin >> T;

	for( int ct = 0; ct < T; ++ct)
	{
		int N = 0;
		cin >> N;

		vector< int > nums;

		for( int i = 0; i < N; ++i )
		{
			int t = 0;
			cin >> t;
			nums.push_back( t );
		}

		int sum = accumulate( nums.begin( ), nums.end( ), 0 );

		int ans = INT_MAX;

		for( int i = 0; i < nums.size( ); ++i )
		{
			int cur = 0;

			for( int j = 0; j < nums.size( ); ++j )
			{
				if( i != j )
				{
					for( int k = 0; k < 32; ++k )
					{
						cur = cur ^ ( nums[ j ] & ( 1  << k ) );
					}
				}
			}

			if( cur == nums[ i ] && cur < ans )
			{
				ans = cur;
			}
		}

		cout << "Case #" << ct + 1 << ": ";

		if( ans == INT_MAX )
		{
			cout << "NO" << endl;
		}
		else
		{
			cout << sum - ans << endl;
		}
	}
}