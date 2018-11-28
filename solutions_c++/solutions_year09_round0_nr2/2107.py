//Arek Wróbel - skater
#include <cstdio>
using namespace std;
int h, w;
int map[102][102];
int tab[102][102][2]; //najpierw y, potem x
int y, x;
int pom;

char lit[101][101];
void debug()
{
	for (int df=1; df<=h; ++df)
		{
			for (int fd=1; fd<=w; ++fd)
				printf("[%2d %2d] ", tab[df][fd][0], tab[df][fd][1]);
			printf("\n");
		}
}
void aktual(const int &py, const int &px)
{
	for (int hj=1; hj<=h; ++hj)
		for (int wj=1; wj<=w; ++wj)
		{
			if (tab[hj][wj][0]==py && tab[hj][wj][1]==px)
			{
				tab[hj][wj][0]=tab[py][px][0];
				tab[hj][wj][1]=tab[py][px][1];
				aktual(hj, wj);
			}
		}
	/*if (tab[py+1][px][0]==py && tab[py+1][px][1]==px)
	{
		tab[py+1][px][0]=tab[py][px][0];
		tab[py+1][px][1]=tab[py][px][1];
		aktual(py+1, px);
	}
	if (tab[py-1][px][0]==py && tab[py-1][px][1]==px)
	{
		tab[py-1][px][0]=tab[py][px][0];
		tab[py-1][px][1]=tab[py][px][1];
		aktual(py-1, px);
	}
	if (tab[py][px+1][0]==py && tab[py][px+1][1]==px)
	{
		tab[py][px+1][0]=tab[py][px][0];
		tab[py][px+1][1]=tab[py][px][1];
		aktual(py, px+1);
	}
	if (tab[py][px-1][0]==py && tab[py][px-1][1]==px)
	{
		tab[py][px-1][0]=tab[py][px][0];
		tab[py][px-1][1]=tab[py][px][1];
		aktual(py, px-1);
	}*/
}
int main()
{
	int t;
	scanf("%d", &t);
	for (int lpt=1; lpt<=t; ++lpt)
	{
		//wej
		scanf("%d%d", &h, &w);
		for (int i=1; i<=h; ++i)
			for (int j=1; j<=w; ++j)
				scanf("%d", &map[i][j]);
		//prog
		//reset
		for (int i=1; i<=h; ++i)
			for (int j=1; j<=w; ++j)
				tab[i][j][0]=tab[i][j][1]=-1;
		for (int i=0; i<=h+1; ++i)
		{
			map[i][0]=20000;
			map[i][w+1]=20000;
		}
		for (int i=0; i<=w+1; ++i)
		{
			map[0][i]=20000;
			map[h+1][i]=20000;
		}
		//
		//debug();
		for (int i=1; i<=h; ++i)
		{
			for (int j=1; j<=w; ++j)
			{
				y=-1;
				x=-1;
				pom=map[i][j];
				if (map[i-1][j]<pom) {
					y=i-1;
					x=j;
					pom=map[y][x];
					}
				if (map[i][j-1]<pom) {
					y=i;
					x=j-1;
					pom=map[y][x];
					}
				if (map[i][j+1]<pom) {
					y=i;
					x=j+1;
					pom=map[y][x];
					}
				if (map[i+1][j]<pom) {
					y=i+1;
					x=j;
					pom=map[y][x];
					}
				
				//printf("aaaaaaaaa\n");
				tab[i][j][0]=y;
				tab[i][j][1]=x;
				
				//debug();
				//printf("\n");
				if (y!=-1 && tab[y][x][0]!=-1)
				{
					tab[i][j][0]=tab[y][x][0];
					tab[i][j][1]=tab[y][x][1];
				}
				if (y!=-1) aktual(i, j);
				
				//debug();
			}
		}
		//zamiana -1 na autoreferencje
		for (int i=1; i<=h; ++i)
			for (int j=1; j<=w; ++j)
				if (tab[i][j][0]==-1)
				{
					tab[i][j][0]=i;
					tab[i][j][1]=j;
				}
		//reset lit
		for (int i=1; i<=h; ++i)
			for (int j=1; j<=w; ++j)
				lit[i][j]=0;
		
		//wstawianie znakow
		char ktlit='a';
		for (int i=1; i<=h; ++i)
			for (int j=1; j<=w; ++j)
			{
				if (lit[i][j]==0) {
					for (int i2=1; i2<=h; ++i2)
						for (int j2=1; j2<=w; ++j2)
							if (tab[i2][j2][0]==tab[i][j][0] && tab[i2][j2][1]==tab[i][j][1]) lit[i2][j2]=ktlit;
					++ktlit;
				}
			}
		//debug();
		//wyj
		printf("Case #%d:\n", lpt);
		for (int i=1; i<=h; ++i)
			for (int j=1; j<=w; ++j)
			{
				printf("%c", lit[i][j]);
				if (j==w) printf("\n"); else printf(" ");
			}
	}
	return 0;
}
