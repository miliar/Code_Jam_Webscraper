#include<iostream>
#include<cstring>
using namespace std;
struct graph
{
	int d;
	graph *next;
};
graph *g[101][101];
int a[101][101];
bool h[101][101];
char ans[101][101];
char cur;
int dx[5],dy[5],x,y,k,minn,d,t,casenum,i,j;
void build(int x,int y,int d)
{
	graph *p=new graph;
	p->d=d;
	p->next=g[x][y];
	g[x][y]=p;
	return;
}
void dfs(int x,int y)
{
	h[x][y]=true;
	ans[x][y]=cur;
	graph *p=g[x][y];
	while (p)
	{
		if (!h[x+dx[p->d]][y+dy[p->d]])
			dfs(x+dx[p->d],y+dy[p->d]);
		p=p->next;
	}
	return;
}
int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	dx[1]=-1;dy[1]=0;dx[2]=0;dy[2]=-1;dx[3]=0;dy[3]=1;dx[4]=1;dy[4]=0;
	scanf("%d\n",&t);
	for (casenum=1;casenum<=t;casenum++)
	{
		scanf("%d%d\n",&x,&y);
		for (i=1;i<=x;i++)
			for (j=1;j<=y;j++)
			{
				scanf("%d",&a[i][j]);
				g[i][j]=NULL;
			}
		for (i=1;i<=x;i++)
			for (j=1;j<=y;j++)
			{
				minn=10000;
				for (k=1;k<=4;k++)
					if (i+dx[k]>0&&i+dx[k]<=x&&j+dy[k]>0&&j+dy[k]<=y&&a[i+dx[k]][j+dy[k]]<minn)
					{
						minn=a[i+dx[k]][j+dy[k]];
						d=k;
					}
				if (minn>=a[i][j]) continue;
				build(i,j,d);
				build(i+dx[d],j+dy[d],5-d);
			}
		memset(h,0,sizeof(h));
		cur='a'-1;
		for (i=1;i<=x;i++)
			for (j=1;j<=y;j++)
				if (!h[i][j])
				{
					cur++;
					dfs(i,j);
				}
		printf("Case #%d:\n",casenum);
		for (i=1;i<=x;i++)
			for (j=1;j<=y;j++)
			{
				if (j==y) printf("%c\n",ans[i][j]);
				else printf("%c ",ans[i][j]);
				graph *p=g[i][j];
				while (p)
				{
					graph *q=p->next;
					delete p;
					p=q;
				}
			}

	}
	return 0;
}
