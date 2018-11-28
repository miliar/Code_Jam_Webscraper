#include <iostream>
#include <queue>
using namespace std;
struct Point
{
	char c;
	int x,y;
};
char map[102][102];
int tt[102][102];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small.out","w",stdout);
	int T,p,n,m,i,j;
	int dire[4][2]={-1,0,0,-1,0,1,1,0};
	scanf("%d",&T);
	for (p=1;p<=T;p++)
	{
		printf("Case #%d:\n",p);
		scanf("%d%d",&n,&m);
		for (i=0;i<n;i++)
		{
			for (j=0;j<m;j++)
			{
				scanf("%d",&tt[i][j]);
				map[i][j] = ' ';
			}
		}
		int result = 0;
		char cChar = 'a';
		queue <Point> que;
		Point a,b,c;
		while (result!=n*m)
		{
			for (i=0;i<n;i++)
			{
				for (j=0;j<m;j++)
				{
					if (map[i][j]==' ') break;
				}
				if (j!=m) break;
			}
			a.x =i;a.y= j;
			a.c = cChar;
			map[a.x][a.y] = a.c;
			cChar++;
			que.push(a);
			while (!que.empty())
			{
				a = que.front();
				que.pop();
				result++;
				int x,y,minx,miny,min=999999999,mind;
				for (i=0;i<4;i++)
				{
					x = a.x + dire[i][0];
					if (x<0||x>=n) continue;
					y = a.y + dire[i][1];
					if (y<0||y>=m) continue;
					if (tt[x][y]<tt[a.x][a.y]&&tt[x][y]<min)
					{
						minx = x;miny = y;min = tt[x][y];mind=i;
					}
					else if (tt[x][y]>tt[a.x][a.y])
					{
						int tx,ty,tmin=999999999,tminx,tminy;
						for (j=0;j<4;j++)
						{
							tx = x + dire[j][0];
							if (tx<0||tx>=n) continue;
							ty = y + dire[j][1];
							if (ty<0||ty>=m) continue;
							if (tt[tx][ty]<tt[x][y]&&tt[tx][ty]<tmin)
							{
								tmin = tt[tx][ty];
								tminx = tx;tminy=ty;
							}
						}
						if (tmin!=999999999&&tminx==a.x&&tminy==a.y)
						{
							if (map[x][y]==' ')
							{
								b.x = x;
								b.y = y;
								b.c = a.c;
								map[b.x][b.y] = b.c;
								que.push(b);
							}

						}
					}
				}
				if (min!=999999999)
				{
					if (map[minx][miny]==' ')
					{
						b.x = minx;b.y = miny;
						b.c = a.c;
						map[b.x][b.y] = b.c;	
						que.push(b);
					}
				}
			}
		}
		for (i=0;i<n;i++)
		{
			for (j=0;j<m;j++)
			{
				if (j!=0) printf(" ");
				printf("%c",map[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}