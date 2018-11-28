#include<stdio.h>
#include<iostream>

using namespace std;

int n;
int h,w;


int m[120][120];
char col[120][120];
char cur;


int dir[][2] = { { -1,0 }, {0,-1},{0,1},{1,0} };

char dfs( int x, int y)
{
	if( col[x][y] )
		return col[x][y];

	int rez = m[x][y];
	int dx,dy ,rx = -1, ry = -1;		
	for( int i=0; i<4; i++ )
	{
		dx =  x + dir[i][0] ;
		dy =  y + dir[i][1] ;
		if( dx< h &&  dx >= 0 && dy< w &&  dy >= 0 )
		{
			if( m[dx][dy] < rez )
			{
				rez = m[dx][dy];
				rx = dx;
				ry = dy;
			}
		} 
			
	}

	if( rx == -1)
	{	/* sink */
		col[x][y] = cur;
		cur++;
		return col[x][y];
	
	}

	col[x][y] = dfs( rx,ry);
		
	return col[x][y];

}



int main(int argc,char ** argv)
{

	freopen ("water.in", "r",stdin);
	freopen ("water.out", "w",stdout);

	scanf("%d",&n);
	

	for( int tt=0;tt<n;tt++)
	{

		scanf("%d",&h);
		scanf("%d",&w);

		memset(col,0,sizeof(col) );

		cur = 'a';

		for( int i=0;i<h;i++)
			for( int j=0;j<w;j++)
				scanf("%d",&m[i][j] );

		printf("Case #%d:\n",tt+1);

		for( int i=0;i<h;i++)
		{
			for( int j=0;j<w;j++)
			{
				printf( "%c ",dfs(i,j) );
			}
			printf("\n");		
		}

		
		
		

	}
	
	return 0;
}

