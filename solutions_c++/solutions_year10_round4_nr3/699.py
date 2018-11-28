#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <math.h>
#pragma comment (linker,"/STACK:16000000")
using namespace std;
const int maxn = 1010;
char mas[maxn+10][maxn+10]={0};
struct pnt{
	int x;
	int y;
};
pnt och[2][110*110];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i,j,n,m,xx,yy,x1,x2,y1,y2;
	scanf("%d\n",&t);
	for (int q=1;q<=t;++q)
	{
		scanf("%d",&n);
		for (i=1;i<=maxn;i++)
			for (j=1;j<=maxn;j++)
				mas[i][j] = mas[i][j] = 0;

		for (i=1;i<=n;i++)
		{
			scanf("%d %d %d %d",&y1,&x1,&y2,&x2);
			for (xx=x1;xx<=x2;xx++)
				for (yy=y1;yy<=y2;yy++)
					mas[xx][yy] = 1; 
		}
		int b[2]={1,1};
		int e[2]={0,0};
		for (i=1;i<=100;i++)
		{
			for (j=1;j<=100;j++)
				if (mas[i][j])
				{
					e[0]++;
					och[0][e[0]].x = i;
					och[0][e[0]].y = j;
				}
		}
		int cnt = 0, cur = 0, fl = 1;
		while (fl)
		{
			fl = 0;
			while (b[cur]<=e[cur])
			{
				fl = 1;
				xx = och[cur][b[cur]].x;
				yy = och[cur][b[cur]].y;
				if (mas[xx][yy-1]==1 || mas[xx-1][yy]==1)
				{
					e[1-cur]++;
					och[1-cur][e[1-cur]].x = xx;
					och[1-cur][e[1-cur]].y = yy;
				}
				if (mas[xx][yy+1]==0 && mas[xx-1][yy+1]==1)
				{
					e[1-cur]++;
					och[1-cur][e[1-cur]].x = xx;
					och[1-cur][e[1-cur]].y = yy+1;
				}
				++b[cur];
			}
			for (i=1;i<=e[cur];i++)
				mas[och[cur][i].x][och[cur][i].y] = 0;
			b[cur] = 1;
			e[cur] = 0;
			cur = 1 - cur;
			for (i=1;i<=e[cur];i++)
				mas[och[cur][i].x][och[cur][i].y] = 1;
			if (fl)
				cnt++;
			b[cur] = 1;
		}

		printf("Case #%d: %d\n",q,cnt);
		fflush(stdout);				
	}
	return 0;
}