#include<stdio.h>
#include<memory.h>
#include <algorithm>
using namespace std;
const int maxn = 1100;

struct cell
{
	int x,p;
};
int n,k;
int price[110][30];
bool can[110][110];
int t,ncase,i,j,l,r,th,ans,s;
cell a[1000];
bool cross(int y1,int y2,int y3,int y4)
{
    if(y1==y3||y2==y4) return true;
    if(y1<y3&&y2>y4) return true;
    if(y1>y3&&y2<y4) return true;
    return false;
}
void init()
{
    int i,j,t;
    scanf("%d%d",&n,&k);
    for(i=1;i<=n;i++)
        for(j=1;j<=k;j++) scanf("%d",&price[i][j]);
	for(i=1;i<=n;i++)
        for(j=i+1;j<=n;j++)
        {
            for(t=1;t<k;t++) if(cross(price[i][t],price[i][t+1],price[j][t],price[j][t+1])) break;
            if(t<k) can[i][j]=can[j][i]=false;
            else can[i][j]=can[j][i]=true;
        }
}

struct Hungary{

	struct cell
	{
		int num,next;
	};

	int N,M,t,ans;
	int a[maxn],y[maxn];
	bool bol[maxn];
	cell E[maxn*maxn];
	void init(int n,int m)
	{
		int i;
		N=n;
		M=m;
		for (i=1;i<=n;i++) a[i]=0;
		t=0;
		ans=0;
	}
	void insert(int x,int y)
	{
		t++;
		E[t].num=y;
		E[t].next=a[x];
		a[x]=t;
	}
	bool find(int p)
	{
		bol[p]=false;
		int i,j;
		for (i=a[p];i;i=E[i].next)
		{
			j=E[i].num;
			if (y[j]==0)
			{
				y[j]=p;
				return true;
			} else
			if (bol[y[j]]&&find(y[j]))
			{
				y[j]=p;
				return true;
			}
		}
		return false;
	}
	void work()
	{
		int i,j;
		for (i=1;i<=M;i++) y[i]=0;
		for (i=1;i<=N;i++)
		{
			for (j=1;j<=N;j++) bol[j]=true;
			if (find(i)) ans++;
		}
	}
} match;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&ncase);
    for(t=1;t<=ncase;t++)
    {
        init();
        printf("Case #%d: ",t);
		match.init(n,n);
		for (i=1;i<=n;i++)
			for (j=1;j<=n;j++)
				if (price[i][1]>price[j][1]&&can[i][j]) match.insert(i,j);
		match.work();
		printf("%d\n",n - match.ans);
    }
	return 0;
}