#include <iostream>
#include <string>
using namespace std;

typedef struct  
{
	int g,c;
	int v;
} tnode;
tnode a[11000];

int n;

int mem[11000][2];

int dfs(int x,int v)
{
	if(mem[x][v]!=-1) return mem[x][v];
	if(x<=(n-1)/2)
	{
		int minn=1<<20;

		if(a[x].c)
		{
			if(v==1)
			{
				minn=min(minn,dfs(x*2,1)+dfs(x*2+1,1) );
				minn=min(minn,dfs(x*2,0)+dfs(x*2+1,1)+(a[x].g?1:0));
				minn=min(minn,dfs(x*2,1)+dfs(x*2+1,0)+(a[x].g?1:0));
			}
			else 
			{
				minn=min(minn,dfs(x*2   ,0)+(a[x].g?0:1));
				minn=min(minn,dfs(x*2+1 ,0)+(a[x].g?0:1));
				minn=min(minn,dfs(x*2,0)+dfs(x*2+1,0));
			}
		}
		else
		{
			if(v==1)
			{
				if(a[x].g)
				{
					minn=min(minn,dfs(x*2,1)+dfs(x*2+1,1));
				}
				else
				{
					minn=min(minn,dfs(x*2,1)+dfs(x*2+1,0));
					minn=min(minn,dfs(x*2,0)+dfs(x*2+1,1));
					minn=min(minn,dfs(x*2,1)+dfs(x*2+1,1));
				}
			}
			else
			{
				if(a[x].g)
				{
					minn=min(minn,dfs(x*2,0)+dfs(x*2+1,1));
					minn=min(minn,dfs(x*2,1)+dfs(x*2+1,0));
					minn=min(minn,dfs(x*2,0)+dfs(x*2+1,0));
				}
				else
				{
					minn=min(minn,dfs(x*2,0)+dfs(x*2+1,0));
				}
			}
		}

		mem[x][v]=minn;
		return minn;

	}
	else
	{
		if(v==a[x].v)
			return 0;
		else 
			return 1<<20;
	}
}

int main()
{
	int T,Ti=0;;
	scanf("%d",&T);
	while(T--)
	{
		Ti++;
		memset(mem,-1,sizeof(mem));
		scanf("%d",&n);
		int v;
		scanf("%d",&v);
		for(int i=1;i<=(n-1)/2;i++)
		{
			int t1,t2;
			scanf("%d%d",&t1,&t2);
			a[i].g=t1;
			a[i].c=t2;
		}
		for(int i=(n-1)/2+1;i<=n;i++)
		{
			scanf("%d",&a[i].v);
		}
		int result=dfs(1,v);
		printf("Case #%d: ",Ti);

		if(result<1<<20)
			printf ("%d\n",result);	
		else
			puts("IMPOSSIBLE");

	}
}