#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

const int MAXN = 102;
const int dr [ ] = { -1 , 0 , 0 , 1 };
const int dc [ ] = {  0 , -1, 1 , 0 };

int h [ MAXN ][ MAXN ];
char lab [ MAXN ][ MAXN ];
int R , C , last ;

bool out(int r,int c)
{
	return r < 0 || r >= R || c < 0 || c >= C ;
}

char draw(int r,int c)
{
	if(lab[r][c]!=-1)
		return lab[r][c];
	int best = -1;
	int low = 10000000;
	int i,nr,nc;
	for(i=0;i<4;i++)
	{
		nr = r + dr[ i ];
		nc = c + dc[ i ];
		if(out(nr,nc))continue;
		if(h[nr][nc]<low)
		{
			low = h[nr][nc];
			best = i ;
		}
	}
	if(low >= h[r][c])
		return lab[r][c]=last+'a';
	else
		return lab[r][c]=draw(r+dr[best],c+dc[best]);
}

int main()
{
	freopen("data.txt", "r", stdin );
	freopen("B.out", "w", stdout );
	int t ;
	scanf ( "%d", &t );
	int cas;

	for( cas = 1; cas <= t; cas ++ )
	{
		memset( lab , -1, sizeof lab );
		scanf ( "%d %d", &R,&C );
		int i , j ;
		last = 0;

		for( i = 0;i < R; i ++ )
			for( j = 0;j < C; j ++ )
				scanf ( "%d", &h[ i ][ j ] );

		for( i = 0;i < R; i ++ )
			for( j = 0;j < C; j ++ )
			{
				if( lab[ i ][ j ] != -1 )
					continue ;
				last += (draw( i , j ) == (last + 'a'));
			}

		printf ( "Case #%d:\n", cas );
		for( i = 0;i < R; i ++ )
		{
			for( j = 0;j < C; j ++ )
			{
				if(j+1<C)
					printf ( "%c ", lab[ i ][ j ]);
				else
					printf ( "%c\n", lab[ i ][ j ] );
			}
		}

	}

	return 0;
}