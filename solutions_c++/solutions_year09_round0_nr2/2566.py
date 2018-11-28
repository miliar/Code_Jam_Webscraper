#include <stdio.h>
#include <string.h>

#define MAXN 128
#define INF 1024*10

enum dir
{
    NONE,
    NORTH,
    WEST,
    EAST,
    SOUTH
};

int brd[MAXN][MAXN];
int flow[MAXN][MAXN];
int resp[MAXN*MAXN];

void paint(int i, int j, int c)
{
    brd[i][j] = c;

    if ( flow[i+1][j] == NORTH )
    {
	paint(i+1,j,c);
    }
    if ( flow[i-1][j] == SOUTH )
    {
	paint(i-1,j,c);
    }
    if ( flow[i][j-1] == EAST )
    {
	paint(i,j-1,c);
    }
    if ( flow[i][j+1] == WEST )
    {
	paint(i,j+1,c);
    }
}

void findFlow(int i, int j)
{
    dir k;
    int temp;// = brd[i][j];
//    k = NONE;

//    if ( brd[i-1][j] <= temp )
    {
	k = SOUTH;
	temp = brd[i+1][j];
    }
    if ( brd[i][j+1] <= temp )
    {
	k = EAST;
	temp = brd[i][j+1];
    }
    if ( brd[i][j-1] <= temp )
    {
	k = WEST;
	temp = brd[i][j-1];
    }
    if ( brd[i-1][j] <= temp )
    {
	k = NORTH;
	temp = brd[i-1][j];
    }

    
    if ( brd[i][j] <= temp )
    {
	k = NONE;
    }
    flow[i][j] = k;
}

int main (void)
{
    int n;
    int h, w;

    scanf("%d",&n);

    for ( int i = 0 ; i < n ; i++ )
    {
	scanf("%d%d",&h, &w);

	for ( int j = 0 ; j <= h+1 ; j++ )
	    for ( int k = 0 ; k <= w+1 ; k++ )
	    {
		brd[j][k] = INF;
		flow[j][k] = NONE;
	    }

	for ( int j = 1 ; j <= h ; j++ )
	{
	    for ( int k = 1 ; k <= w ; k++ )
	    {
		scanf("%d",&brd[j][k]);
	    }
	}

	for ( int j = 1 ; j <= h ; j++ )
	{
	    for ( int k = 1 ; k <= w ; k++ )
	    {
		findFlow(j,k);
//		printf("%d ",flow[j][k]);
	    }
//	    printf("\n");
	}
//	printf("\n");
	int basins;
	basins = 0;

	for ( int j = 1 ; j <= h ; j++ )
	{
	    for ( int k = 1 ; k <= w ; k++ )
	    {
		if ( flow[j][k] == 0 ) paint(j,k,basins++);
	    }
	}

	memset(resp, 0xFF, sizeof(resp));
	int r = 0;

	printf("Case #%d:\n",i+1);

	for ( int j = 1 ; j <= h ; j++ )
	{
	    for ( int k = 1 ; k <= w ; k++ )
	    {
		if ( resp[brd[j][k]] == -1  ) { resp[brd[j][k]] = r++; }
		printf("%c ",resp[brd[j][k]]+'a');
	    }
	    printf("\n");
	}
    }

    return 0;
}

