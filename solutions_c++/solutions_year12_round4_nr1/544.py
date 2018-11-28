
#include <iostream>

#include <vector>
#include <string>

#include <utility>
#include <queue>

using namespace std;

int tests;

int N;
vector<long long> d, l;
long long D;
queue< pair< int, long long > > q;

long long dp[10000+1];


int main()
{
	cin >> tests;

	for( int curTest=0; curTest<tests; ++curTest )
	{

		cin >> N;
		d = l = vector<long long>( N+1 );
		for( int i=0; i<N; ++i )
			cin >> d[i] >> l[i];
		cin >> D;
		d[N] = D;
		l[N] = D;

		while( !q.empty() )
			q.pop();

		memset( dp, -1, sizeof(dp) );

		bool res = false;
		q.push( make_pair( 0, min( d[0], l[0] ) ) );
		while( !q.empty() )
		{
			const int idx = q.front().first;
			const int idD = q.front().second;
			q.pop();
			int fidx = -1;
			long long fidD = -1;
			for( int i=idx+1; i<=N; ++i )
			{
				if ( d[i]-d[idx] <= idD )
				{
					if ( i == N )
					{
						res = true;
						break;
					}
					if ( dp[i] < min( d[i]-d[idx], l[i] ) )
					{
						q.push( make_pair( i, min( d[i]-d[idx], l[i] ) ) );
						dp[i] = min( d[i]-d[idx], l[i] );
					}
				}
			}
			if ( res )
				break;
		}

		cout << "Case #" << (curTest+1) << ": ";
		cout << (res?"YES":"NO");
		cout << endl;
	}

	return 0;
}

