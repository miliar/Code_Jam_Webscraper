#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

const int MAXN = 5005;

char dict[MAXN][20];
bool on[20][30];
int N,L,D;

int main()
{
	freopen("data.txt", "r", stdin );
	freopen("A.out", "w", stdout );
	scanf ( "%d %d %d" , &L, &D, &N );
	int i , j , k ;

	for( i = 0;i < D; i ++ )
		scanf ( "%s", dict[ i ] );

	for( i = 0;i < N; i ++ )
	{
		char pat[400];
		scanf ( "%s", pat );
		int len = strlen( pat );
		int at = 0;
		bool ins = false;
		memset( on , 0, sizeof on );
		for( j = 0;j < len; j++)
		{
			if( pat[ j ] == '(')
			{
				ins = true;
				continue ;
			}
			if( pat[ j ] == ')')
			{
				ins = false;
				at ++;
				continue;
			}
			on[ at ][ pat[ j ] - 'a' ] = true ;
			at += !ins;
		}
		int res=  0;

		for( j = 0;j < D; j ++ )
		{
			bool yes = true;
			for( k = 0;k < L; k ++)
				if( !on[k][ dict[j][k] - 'a' ] )
					yes = false ;
			res += yes ;
		}

		printf ( "Case #%d: %d\n", i + 1 , res );
	}

	return 0;
}