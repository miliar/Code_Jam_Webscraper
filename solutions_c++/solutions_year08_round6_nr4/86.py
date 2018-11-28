#define _CRT_SECURE_NO_WARNINGS

#include<vector>
#include<map>
#include<string>
#include<cstdio>
#include<cstring>
#include<cstdlib>

using namespace std;

#define MAXN 10
bool con1[MAXN][MAXN];
int con2[MAXN][MAXN];
int p[MAXN];
bool used[MAXN];
int n1, n2;
int cnt2[MAXN];

bool find_it( int q )
{
	int i, j;
	if( q == n2 )
	{
		for( i = 0; i < n2; ++i )
			for( j = 0; j < cnt2[i]; ++j )
			{
				int s = con2[i][j];
				if( !con1[p[i]][p[s]] )
					return false;
			}
		return true;
	}
	for( i = 0; i < n1; ++i )
		if( !used[i] )
		{
			used[i] = true;
			p[q] = i;
			if( find_it( q + 1 ) )
				return true;
			used[i] = false;
		}
	return false;
}

void make_it()
{
	memset( con1, 0, sizeof( con1 ) );
	memset( con2, 0, sizeof( con2 ) );
	memset( cnt2, 0, sizeof( cnt2 ) );
	memset( used, 0, sizeof( used ) );

	scanf( "%d", &n1 );
	int i, a, b;
	for( i = 0; i < n1 - 1; ++i )
	{
		scanf( "%d %d", &a, &b );
		--a;
		--b;
		con1[a][b] = true;
		con1[b][a] = true;
	}

	scanf( "%d", &n2 );
	for( i = 0; i < n2 - 1; ++i )
	{
		scanf( "%d %d", &a, &b );
		--a;
		--b;
		con2[a][cnt2[a]++] = b;
		con2[b][cnt2[b]++] = a;
	}

	if( find_it( 0 ) )
		printf( "YES\n" );
	else
		printf( "NO\n" );
}

int main()
{
	freopen( "d1_2.in", "r", stdin );
	freopen( "out.out", "w", stdout );

	int test = 0;
	scanf( "%d", &test );
	for( int i = 1; i <= test; ++i )
	{
		printf( "Case #%d: ", i );
		make_it();
	}
	return 0;
}
