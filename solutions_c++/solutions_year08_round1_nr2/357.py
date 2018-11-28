#include<iostream>
using namespace std;

#define maxn 102

int n,m;
int best;
int ans[maxn];
int tans[maxn],cnt[maxn];
int like[maxn][3002],type[maxn][3002];

void mysort(int x)
{
	int i,j;
	int tcnt =0 ;
	for(i=0;i<cnt[x];i++)
	{
		if(type[x][i] == 0)
			tcnt++;
	}
	for(j=tcnt,i=0;i<tcnt;i++)
	{
		if(type[x][i] == 1)
		{
			while(type[x][j] == 1)
				j++;
			swap(type[x][j],type[x][i]);
			swap(like[x][j],like[x][i]);
		}
	}
	return;
}
void tsort()
{
	int i,j,k;
	for(i=0;i<m;i++)
	{
		for(j=i+1;j<m;j++)
		{
			if(cnt[i]>cnt[j])
			{
				for(k=0;k<cnt[i];k++)
				{
					swap(type[i][k],type[j][k]);
					swap(like[i][k],like[j][k]);
				}
				swap(cnt[i],cnt[j]);
			}
		}
	}
	/*
	for(i=0;i<m;i++)
	{
		printf("%d\n",cnt[i]);
		for(j=0;j<cnt[i];j++)
			printf("%d %d   ",like[i][j],type[i][j]);
		puts("");
	}*/
	return;
}

void dfs(int x,int is)
{
	if(is>=best)
		return; 
	int i,k,t;
	if(x == m)
	{
		best = is;
		for(i=0;i<n;i++)
			ans[i] = tans[i];
		return ;
	}
	for(i=0;i<cnt[x];i++)
	{
		k = like[x][i];
		t = type[x][i];
		if(tans[k] == -1)
		{
			tans[k] = t;
			dfs(x+1,is+ (t==1?1:0));
			tans[k] = -1;
		}
		else if(tans[k] == t)
		{
			dfs(x+1,is);
		}
	}
	return;
}
int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int ii,cas,i,j;
	scanf("%d",&cas);
	for(ii=1;ii<=cas;ii++)
	{
		scanf("%d",&n);
		scanf("%d",&m);
		for(i=0;i<m;i++)
		{
			scanf("%d",&cnt[i]);
			for(j=0;j<cnt[i];j++)
			{
				scanf("%d%d",&like[i][j],&type[i][j]);
				like[i][j] --;
			}
			mysort(i);
		}
		tsort();
		best = maxn+1;
		memset(tans,-1,sizeof(tans));
		memset(ans,-1,sizeof(ans));
		dfs(0,0);
		printf("Case #%d:",ii);
		if(best == maxn+1)
			printf(" IMPOSSIBLE\n");
		else
		{
			for(i=0;i<n;i++)
			{
				if(ans[i] == -1)
					ans[i] =0 ;
				printf(" %d",ans[i]);
			}
			puts("");
		}
	}
	return 0;
}