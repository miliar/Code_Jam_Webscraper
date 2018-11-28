
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

#define MAX 128

int alt[MAX][MAX];
int basin[MAX][MAX];

char mapa[MAX];

int cnt = 0;

int b(int x, int y)
{
	if(basin[x][y] != -1) return basin[x][y];

	int mi = alt[x][y];
	int nx, ny;

	if(alt[x-1][y] < mi){mi=alt[x-1][y]; nx=x-1; ny=y;}
	if(alt[x][y-1] < mi){mi=alt[x][y-1]; nx=x; ny=y-1;}
	if(alt[x][y+1] < mi){mi=alt[x][y+1]; nx=x; ny=y+1;}
	if(alt[x+1][y] < mi){mi=alt[x+1][y]; nx=x+1; ny=y;}

	//printf("%d %d (%d) mi=%d\n", x, y, alt

	if(mi != alt[x][y])
	{
		basin[x][y] = b(nx, ny);
	}
	else
	{
		basin[x][y] = cnt++;
	}

	return basin[x][y];
}

int main(void)
{
	int t;
	int h, w;
	int i, j;
	int ca;

	scanf("%d", &t);
	for(ca=1; ca<=t; ca++)
	{
		printf("Case #%d:\n", ca);

		scanf("%d %d", &h, &w);

		memset(alt, 0x3f, sizeof(alt));

		for(i=1; i<=h; i++)
		{
			for(j=1; j<=w; j++)
			{
				scanf("%d", &alt[i][j]);
			}
		}

		memset(basin, -1, sizeof(basin));
		cnt = 0;

		for(i=1; i<=h; i++)
			for(j=1; j<=w; j++)
				b(i, j);

		char c = 'a';
		memset(mapa, 0, sizeof(mapa));
		for(i=1; i<=h; i++)
		{
			for(j=1; j<=w; j++)
			{
				if(mapa[basin[i][j]] == 0)
				{
					mapa[basin[i][j]] = c++;
				}

				if(j > 1) printf(" ");

				printf("%c", mapa[basin[i][j]]);
				//printf("%d", basin[i][j]);
			}

			printf("\n");
		}
	}

	return 0;
}
