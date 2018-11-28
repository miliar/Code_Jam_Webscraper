#include "iostream"
#include "algorithm"
#include "cstring"
#include "stack"
#include "queue"
#include "set"
#define N 101
#define M 101
using namespace std;
int h,w,basin;
int altitude[N][N];
int label[N][N];
bool u[N][N];
int xx[4]={-1,0,0,1};
int yy[4]={0,-1,1,0};
void init()
{
	int i,j;
	basin=0;
	memset(label,-1,sizeof(label));
	memset(u,false,sizeof(u));
	scanf("%d%d",&h,&w);
	for(i=0;i<h;i++)
		for(j=0;j<w;j++)
			scanf("%d",&altitude[i][j]);
}
int find(int x,int y)
{
	int i,low=-1;
	if(label[x][y]!=-1)
		return label[x][y];
	for(i=0;i<4;i++)
	{
		int ii=x+xx[i];
		int jj=y+yy[i];
		if(ii>=0&&jj>=0&&ii<h&&jj<w&&!u[ii][jj])
		{
			if(low!=-1)
			{
				if(altitude[ii][jj]<altitude[x+xx[low]][y+yy[low]])
					low=i;
			}
			else
			{
				if(altitude[ii][jj]<altitude[x][y])
					low=i;
			}
		}
	}
	if(low==-1)
	{
		basin++;
		label[x][y]=basin-1;
		return basin-1;
	}
	else
	{
		int t;
		u[x][y]=true;
		t=find(x+xx[low],y+yy[low]);
		label[x][y]=t;
		u[x][y]=false;
		return t;
	}
}
void solve()
{
	int i,j;
	for(i=0;i<h;i++)
	{
		for(j=0;j<w;j++)
		{
			if(label[i][j]==-1)
			{
				find(i,j);
			}
		}
	}
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int n,ncase;
	scanf("%d",&n);
	for(ncase=1;ncase<=n;ncase++)
	{
		int i,j;
		init();
		solve();
		printf("Case #%d:\n",ncase);
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				putchar(label[i][j]+'a');
				putchar(' ');
//				printf("%c ",(char)(label[i][j]+'a'));
			}
			putchar('\n');
		}
	}
	return 0;
}