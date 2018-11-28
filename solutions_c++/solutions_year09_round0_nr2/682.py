#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<queue>

using namespace std;

typedef long long ll;

const int MAX=200;
const int INF=1000000000;

const int dir[][2]=
{
	{-1,0},{0,-1},{0,1},{1,0}
};

int alt[MAX][MAX];
int e[MAX][MAX];
int tag[MAX][MAX];
int h,w;
int color;
struct Point
{
	int x,y;
	Point (int a=0,int b=0):x(a),y(b){}
};
queue<Point>que;

void BFS(int x,int y,int col)
{
	tag[x][y]=col;

	while (!que.empty()) que.pop();
	que.push(Point(x,y));
	int i,j;
	Point cur,tmp;

	while (!que.empty())
	{
		cur=que.front();
		que.pop();

		for (i=0;i<4;i++)
		{
			tmp.x=cur.x+dir[i][0];
			tmp.y=cur.y+dir[i][1];
			if (tmp.x<=0 || tmp.x>h || tmp.y<=0 || tmp.y>w || tag[tmp.x][tmp.y]!=-1) continue;
			if (e[tmp.x][tmp.y]==3-i || e[cur.x][cur.y]==i)
			{
				tag[tmp.x][tmp.y]=col;
				que.push(tmp);
			}
		}
	}
}


int main()
{
	int i,j;
	int cas;
	int t;
	int d,x,y;
	int low,id;
	

	freopen("in","r",stdin);
	freopen("out","w",stdout);

	scanf("%d",&t);
	for (cas=1;cas<=t;cas++)
	{
		scanf("%d%d",&h,&w);
		for (i=0;i<=h+1;i++)
			for (j=0;j<=w+1;j++)
			{
				alt[i][j]=INF;
				e[i][j]=-1;
				tag[i][j]=-1;
			}

		for (i=1;i<=h;i++)
			for (j=1;j<=w;j++)
				scanf("%d",&alt[i][j]);

		for (i=1;i<=h;i++)
			for (j=1;j<=w;j++)
			{
				id=0;
				low=alt[i+dir[0][0]][j+dir[0][1]];
				for (d=1;d<4;d++)
				{
					x=i+dir[d][0];
					y=j+dir[d][1];
					if (alt[x][y]<low)
					{
						id=d;
						low=alt[x][y];
					}					
				}
				if (low<alt[i][j])  //no a sink
				{
					e[i][j]=id;
				}
			}

			//for (printf("Show E:\n"),i=1;i<=h;i++,putchar('\n'))
			//for (j=1;j<=w;j++)
			//	printf("%d ",e[i][j]);


		color=0;
		for (i=1;i<=h;i++)
			for (j=1;j<=w;j++)
				if (tag[i][j]==-1)
				{
					BFS(i,j,color);
					color++;
				}
		printf("Case #%d:\n",cas);
		for (i=1;i<=h;i++)
		{
			printf("%c",char(tag[i][1]+'a'));
			for (j=2;j<=w;j++)
				printf(" %c",char(tag[i][j]+'a'));
			printf("\n");
		}
				
	}

	return 0;
}