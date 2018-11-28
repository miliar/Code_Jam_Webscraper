
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

const int dx[] = { -1, 0, 0, 1};

const int dy[] = { 0, -1, 1, 0};

int map[101][101], H, W;
int father[101][101][2];
int lable[101][101];

void find( int i, int j, int & I, int & J )
{
	while ( father[i][j][0] != -1 && father[i][j][1] != -1 )
	{
		I = father[i][j][0], J = father[i][j][1];
		i = I, j = J;
	}
	I = i, J = j;
}

void link( int i0, int j0, int i1, int j1 )
{
	int fi0, fj0, fi1, fj1;
	find( i0, j0, fi0, fj0 );
	find( i1, j1, fi1, fj1 );
	if ( fi0 != fi1 || fj0 != fj1 )
	{
		father[fi1][fj1][0] = fi0;
		father[fi1][fj1][1] = fj0;
	}
}

int main()
{
	int i,j,k,l,pi,pj,T;
	freopen("C:\\B-large.in","r",stdin);
	freopen("C:\\B-large.out","w",stdout);
	scanf("%d",&T);
	for ( i = 1; i <= T; i++ )
	{
		scanf("%d%d",&H,&W);
		for ( j = 0; j < H; j++ )
		{
			for ( k = 0; k < W; k++ )
			{
				scanf("%d",&map[j][k]);
			}
		}
		memset( father, -1, sizeof(father) );
		memset( lable, -1, sizeof(lable) );
		for ( j = 0; j < H; j++ )
		{
			for ( k = 0; k < W; k++ )
			{		
				int ri = -1,rj = -1;
				int r = 0x7FFFFFFF;
				for ( l = 0; l < 4; l++ )
				{
					pi = j + dx[l];
					pj = k + dy[l];
					if ( pi>=0 && pi<H && pj>=0 && pj<W )
					{
						if ( map[pi][pj] < map[j][k] && r > map[pi][pj] )
						{
							r = map[pi][pj];
							ri = pi;
							rj = pj;
						}
					}

				}			
				if ( ri != -1 && rj != -1 )
				{
					link( ri, rj, j, k );
				}
				//printf(" %d %d\n", ri, rj);
			}
		}
		l = 0;
		printf("Case #%d:\n",i);
		for ( j = 0; j < H; j++ )
		{
			for ( k = 0; k < W; k++ )
			{
				find( j, k, pi, pj );
				//printf("%d %d\n", pi, pj);
				if ( lable[pi][pj] == - 1 )
				{
					lable[pi][pj] = l++;
				}
				printf ( "%c ", char(lable[pi][pj]+'a'));
			}
			printf("\n");
		}
	}
	return 0;
}