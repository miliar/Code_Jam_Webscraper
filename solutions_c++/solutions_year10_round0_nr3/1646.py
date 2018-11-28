#include <iostream>
#include <vector>
#include <queue>
using namespace std;




int main( )
{
	freopen( "C.in", "rt", stdin );
	freopen( "C.out", "wt", stdout );

	int T = 0;
	cin >> T;

	for( int ct = 0; ct < T; ++ct )
	{
		int R = 0, k = 0, N = 0;

		cin >> R >> k >> N;

		queue<int> q;

		for( int i = 0; i < N; ++i )
		{
			int x = 0;
			cin >> x;
			q.push( x );
		}

		vector<pair<long long,int>> mem( N, make_pair(-1,-1) );

		int first = 0;

		long long res = 0;

		for( int i = 0; i < R; ++i )
		{
			long long capacity = 0;

			int s = q.size( );

			if( mem[ first ].first != -1 )
			{
				res += mem[ first ].first;
				first = mem[ first ].second;
				continue;
			}

			int advances = 0;

			while( capacity <= k && s > 0 )
			{
				int cur = q.front( );

				capacity += cur;

				if( capacity <= k )
				{
					q.pop( );
					q.push( cur );
					--s;
					advances++;
				}
				else
				{
					capacity -= cur;
					break;
				}
			}

			res += capacity;
			mem[ first ] = make_pair( capacity, ( first + advances ) % N );
			first = ( first + advances ) % N;
		}

		cout << "Case #" << ct + 1 << ": " << res << endl;
	}
}