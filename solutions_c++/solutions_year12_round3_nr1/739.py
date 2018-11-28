#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<queue>
#include<stack>
#include<string>
#include<stdlib.h>
#include<vector>
#include<math.h>
using namespace std;
vector<int> v[1010];
int ans[1010]={0};
void dfs(int p)
{
	ans[p]++;
	if(ans[p]==1)
	{
		for(int i=0;i<v[p].size();i++)
			dfs(v[p][i]);
	}
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("ans.out","w",stdout);
	int t,k=0;
	scanf("%d",&t);
	while(t--)
	{
		k++;
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			v[i].clear();
			int x;
			scanf("%d",&x);
			for(int j=0;j<x;j++)
			{
				int y;
				scanf("%d",&y);
				v[i].push_back(y-1);
			}
		}
		bool sb=0;
		for(int i=0;i<n;i++)
		{
			memset(ans,0,sizeof(ans));
			dfs(i);
			for(int i=0;i<n;i++)
			{
				if(ans[i]>=2)
				{
					sb=1;
					break;
				}
			}
			if(sb)
				break;
		}
		if(sb)
			printf("Case #%d: Yes\n",k);
		else
			printf("Case #%d: No\n",k);
	}
}