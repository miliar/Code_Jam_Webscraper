#include <stdio.h>
#include <set>
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int case_num, n, m;
	
	freopen( "D:\\output.txt", "w", stdout );

	scanf( "%d", &case_num );
	char w[1000];
	vector< vector<int> > hits;

	for( int k=1; k<=case_num; ++k )
	{
		map<string, int> se;
		scanf( "%d", &n );
		getchar();


		for( int i=0; i<n; ++i )
		{
			gets(w);
			se[w] = i;
		}

		scanf( "%d", &m );
		getchar();

		hits.resize( n );

		for( int i=0; i<n; ++i )
		{
			hits[i].resize(0);
		}

		for( int i=0; i<m; ++ i )
		{
			gets( w );
			if( se.find( w ) != se.end() )
			{
				hits[ se[w] ].push_back( i );
			}
		}

		for( int i=0; i<n; ++ i )
		{
			hits[i].push_back( m );
		}

		int ans = 0;
		int curr = 0;
		vector<int> cursor( n, 0 );
		
		while( curr < m )
		{
			int best = 0;
			for( int i=0; i<n; ++i )
			{
				while( cursor[i] < hits[i].size() && hits[i][cursor[i] ] < curr )
				{
					++cursor[i];
				}

				if( hits[best][cursor[best]] < hits[i][cursor[i]] )
				{
					best = i;
				}
			}

			++ans;
			curr = hits[best][cursor[best]];
		}

		if( ans < 1 )
			ans = 1;

		printf( "Case #%d: %d\n", k, ans-1 );
	}

	return 0;
}
