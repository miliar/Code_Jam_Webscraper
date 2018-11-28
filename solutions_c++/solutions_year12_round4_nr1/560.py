#include <cstdio>
#include <cstring>
#include <queue>

using namespace std;

typedef pair<int,int> pii;

int n, D;
priority_queue<pii> pq;

int ml[100020];
int d[100020], l[100020];

int ia( int x )
{
	if ( x < 0 ) return -x;
	return x;
}

bool gogo()
{
	int i, k;
	pii a;
	int v;
	
	pq.push( make_pair( d[1], 1 ) );
	
	while ( pq.size() > 0 )
	{
		a = pq.top();
		pq.pop();
		
		if ( ml[ a.second ] > a.first )
			continue;
		ml[ a.second ] = a.first;
		v = a.second;
		k = a.first;
		if ( k + d[v] >= D )
			return true;
			
		for ( i = 1; i <= n; i++ )
		{
			if ( ( d[i] >= d[v] - k ) && ( d[i] <= d[v] + k ) )
			{
				if ( min( l[i], ia( d[i] - d[v] ) ) > ml[i] )
				{
					ml[i] = min( l[i], ia( d[i]-d[v] ) );
					pq.push( make_pair( ml[i], i ) );
				}
			}
		}
	}
	return false;
}

int main()
{
	int t, T;
	int i;
	
	scanf( "%d", &T );
	for ( t = 1; t <= T; t++ )
	{
		scanf( "%d", &n );
		for ( i = 1; i <= n; i++ )
		{
			scanf( "%d %d", &d[i], &l[i] );
		}
		scanf( "%d", &D );
		
		memset( ml, -1, sizeof( ml ) );
		while ( pq.size() > 0 ) pq.pop();
		
		printf( "Case #%d: ", t );
		if ( gogo() )
		{
			printf( "YES\n" );
		}
		else printf( "NO\n" );
	}
	return 0;
}
