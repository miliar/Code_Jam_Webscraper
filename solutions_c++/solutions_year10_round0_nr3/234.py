#include<stdio.h>

int dat[1024];
int inc[1024];
int tot[1024];

int main()
{
	freopen( "C-large.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int t, r, k, n;

	scanf( "%d", &t );

	for(int i = 0; i < t; ++i )
	{
		scanf( "%d %d %d", &r, &k, &n );
		for( int j = 0; j < n; ++j )
			scanf( "%d", &dat[j] );
		for( int j = 0; j < n; ++j )
		{
			int s = dat[j];
			inc[j] = 1;
			for( int l = 1; l < n; ++l )
				if( s + dat[(j+l)%n] <= k )
				{
					++inc[j];
					s += dat[(j+l)%n];
				}
				else
					break;
			tot[j] = s;
		}
		__int64 s = 0;
		int now = 0;
		for( int j = 0; j < r; ++j )
		{
			s += tot[now];
			now = (now + inc[now]) % n;
		}
		printf( "Case #%d: %I64d\n", i + 1, s );
	}
	return 0;
}