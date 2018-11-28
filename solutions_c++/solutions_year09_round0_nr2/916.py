#include <iostream>
#include <string.h>
#include <fstream>

using namespace std;

int Y,X;
int in[105][105];
int res[105][105][2];
char labl[105][105];

void go (int y, int x)
{
	int a,b,mn=1<<29;
	for (int i1=-1;i1<=1;i1++)
		for (int i2=-1;i2<=1;i2++)
			if (max(i1,-i1)+max(i2,-i2)==1)
			{
				if (in[y+i1][x+i2]<mn)
				{
					mn=in[y+i1][x+i2];
					a=y+i1;
					b=x+i2;
				}
			}
	
	if (mn>=in[y][x])
	{
		res[y][x][0]=y;
		res[y][x][1]=x;
	}

	else

	{
	if (res[a][b][0]==-1)
		go (a,b);
		res[y][x][0]=res[a][b][0];
		res[y][x][1]=res[a][b][1];
	}
	
}


int main ()
{
	freopen ("a.in", "r", stdin);
	freopen ("b.out", "w", stdout);
	int cas;
	scanf("%d", &cas );

	for (int cs=1;cs<=cas;cs++)
	{
		memset (in,63, sizeof(in));
		memset(res,-1, sizeof (res) );
		memset (labl, 0,sizeof(labl));

		scanf("%d%d", &Y, &X);
		for (int i=1;i<=Y; i++)
			for (int j=1;j<=X;j++)
			{
				scanf("%d", &in[i][j]);
			}
		for (int i=1;i<=Y;i++)
			for(int j=1;j<=X;j++)
				if (res[i][j][0]==-1)
				{
					go (i,j);
				}
		char la='a';

		for (int i=1;i<=Y;i++)
			for (int j=1;j<=X;j++)
			{
				if (labl[res[i][j][0]][res[i][j][1]]==0)
				{
					labl[res[i][j][0]][res[i][j][1]]=la;
					la++;
				}
			}

		printf("Case #%d:\n",cs );

		for (int i=1;i<=Y;i++)
			for (int j=1;j<=X;j++)
			{
				printf("%c", labl[res[i][j][0]][res[i][j][1]]);
				if (j==X)
					printf("\n");
				else
					printf(" ");
			}

	}

	return 0;
}
