#include <iostream>
#include <vector>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;
int Case;
int solve(int R,int k,int n)
{
	queue<int> q;
	int i;
	int sum=0;
	for(i=0;i<n;i++)
	{
		int x;
		scanf("%d",&x);
		q.push(x);
		sum+=x;
	}
	if(sum<=k)
		return R*sum;
	int ans=0,cur=0;
	while(R)
	{
		int y=q.front();
		cur+=y;
		if(cur>=k)
		{
			R--;
			if(cur==k)
			{
				ans+=cur;
				cur=0;
			}
			else
			{
				cur-=y;
				ans+=cur;
				cur=y;
			}
		}
		q.pop();
		q.push(y);
	}
	return ans;
}
int main()
{
	scanf("%d",&Case);
	for(int i=1;i<=Case;++i)
	{
		int R,k,n;
		scanf("%d%d%d",&R,&k,&n);
		int ans=solve(R,k,n);
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
