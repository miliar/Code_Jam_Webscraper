#include <iostream>
using namespace std;

const int dis[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
struct point
{
	int h,fx,fy;
	char use;
}p[110][110]={0};

char ch;
int ncase,t,n,m,i,j,k,h,pos,x,y,tempy,tempx;

void getfa(int x, int y)
{
	if (p[x][y].fx==x && p[x][y].fy==y)
		return;
	getfa(p[x][y].fx,p[x][y].fy);
	tempx = p[p[x][y].fx][p[x][y].fy].fx;
	tempy = p[p[x][y].fx][p[x][y].fy].fy;
	p[x][y].fx = tempx;
	p[x][y].fy = tempy;
	return;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&ncase);
	for (t=1; t<=ncase; t++)
	{
		memset(p,0,sizeof(p));
		scanf("%d%d",&n,&m);
		for (i=1; i<=n; i++)
			for (j=1; j<=m; j++)
			{
				scanf("%d",&p[i][j].h);
				p[i][j].fx = i;
				p[i][j].fy = j;
			}
		for (i=1; i<=n; i++)
			for (j=1; j<=m; j++)
			{
				h = p[i][j].h;
				pos = -1;
				for (k=0; k<4; k++)
				{
					if (i+dis[k][0]<1 || i+dis[k][0]>n || j+dis[k][1]<1 || j+dis[k][1]>m)
						continue;
					if (p[i+dis[k][0]][j+dis[k][1]].h<h)
					{
						h = p[i+dis[k][0]][j+dis[k][1]].h;
						pos = k;
					}
				}
				if (pos==-1)
					continue;
				getfa(i,j);
				x = i+dis[pos][0];
				y = j+dis[pos][1];
				getfa(x,y);
				tempx = p[i][j].fx;
				tempy = p[i][j].fy;
				p[tempx][tempy].fx = x;
				p[tempx][tempy].fy = y;
			}
		ch='a';

		for (i=1; i<=n; i++)
			for (j=1; j<=m; j++)
			{
				getfa(i,j);
				if (p[p[i][j].fx][p[i][j].fy].use==0)
					p[p[i][j].fx][p[i][j].fy].use = ch++;
				p[i][j].use = p[p[i][j].fx][p[i][j].fy].use;
			}
		printf("Case #%d:\n",t);
		for (i=1; i<=n; i++)
		{
			for (j=1; j<m; j++)
				printf("%c ",p[i][j].use);
			printf("%c\n",p[i][j].use);
		}
	}
	return 0;
}