#include<iostream>
#include<cstdio>

using namespace std;

int t[110], v[110];

int main()
{
	freopen( "test.in", "r", stdin );
	freopen( "test.out", "w", stdout );
	int N;
	scanf( "%d", &N );
	for (int i = 0; i < N; i++ )
	{
		int n, s, p;
		scanf( "%d %d %d", &n, &s, &p );
		for (int j = 0; j < n; j++ )
			scanf( "%d", &t[j] );
		for (int j = 0; j < n; j++ )
		{
			if (t[j] >= 2 * max(p - 1, 0) + p) v[j] = 2;
			else if (t[j] >= 2 * max(p - 2, 0) + p) v[j] = 1;
			else v[j] = 0;
		}
		int ans = 0, cnt = 0;
		for (int j = 0; j < n; j++ )
		{
			if ( v[j] == 2 ) ans ++;
			if ( v[j] == 1 ) cnt ++;
		} 
		printf( "Case #%d: %d\n", i + 1, ans + min(cnt, s) );
	} 
}
 