#include<iostream>
using namespace std;
#define MAX 15
bool vis[MAX+5];
int _max,n,c[MAX+5];
void dfs(int index)
{
	if(index==n)
	{
		int cnt=0,i;
		for(i=0;i<n;i++)
			if(vis[i])
				cnt++;
		if(cnt==0||cnt==n)
			return;
		int sum1=0,sum2=0,sum=0;
		for(i=0;i<n;i++)
			if(vis[i])
			{
				sum1^=c[i];
				sum+=c[i];
			}
			else
				sum2^=c[i];
		if(sum1==sum2)
			_max=max(_max,sum);
		return;
	}
	dfs(index+1);
	vis[index]=true;
	dfs(index+1);
	vis[index]=false;
}
int main()
{
	int cas,i;
	//freopen("c_s.in","r",stdin);
	//freopen("2.txt","w",stdout);
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d",&c[i]);
		memset(vis,false,sizeof(vis));
		_max=0;
		dfs(0);
		if(_max==0)
			printf("Case #%d: NO\n",ii);
		else
			printf("Case #%d: %d\n",ii,_max);
	}
	return 0;
}