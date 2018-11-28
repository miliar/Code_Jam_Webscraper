#include<iostream>
#include<cstdio>
#include<queue>
#include<memory.h>
#include<math.h>
using namespace std;

struct Node
{
	int d,l;
}node[10010];
struct LR
{
	int l,r;
//	int vd;
}index;
queue<LR>myque;
bool vis[10010];

int dis[10010];

int abs(int a)
{
	if(a<0)a = 0-a;
	return a;
}

int main()
{
	int T;
	freopen("A-large.in","r",stdin);
	freopen("al0.out","w",stdout);
	scanf("%d",&T);
	int icas,n;
	int rangl,rangr;
	int dd;
	bool win;
	for(icas = 1;icas<=T;icas++)
	{
		win = false;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d%d",&node[i].d,&node[i].l);
		}
		scanf("%d",&dd);
		memset(vis,0,sizeof(vis));
		memset(dis,0,sizeof(dis));
		dis[0] = min(node[0].d,node[0].l);
		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
			{
				int tp1 = node[j].d-node[i].d;
				if(dis[i]>=tp1)
				{
					int tp2 = min(tp1,node[j].l);
					dis[j] = max(dis[j],tp2);
				}
			}
		}
		for(int i=0;i<n;i++)
		{
			if((dd>=node[i].d-dis[i])&&(dd<=node[i].d+dis[i]))
			{
	//			cout<<node[i].d<<" "<<dis[i]<<endl;
				win = true;
				break;
			}
		}

		if(win)
		{
			printf("Case #%d: YES\n",icas);
		}
		else printf("Case #%d: NO\n",icas);
	}
	return 0;
}
