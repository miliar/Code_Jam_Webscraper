#include<iostream>
#include<stdio.h>
#include<memory.h>
#include<algorithm>
using namespace std;
struct pt
{
	int v,id;
	bool operator<(const pt &rhs)const
	{
       return v<rhs.v;
	}
};
pt a[1005];
int rank[1005];
double dp[1005];
bool used[1005];
void calc_dp()
{
}
int main()
{
	int n,i,j,tcase,cas;
	calc_dp();
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
    cin>>tcase;
	for(cas=1;cas<=tcase;cas++)
	{
        cin>>n;
		for(i=1;i<=n;i++)
		{
			cin>>a[i].v;
		    a[i].id=i;
		}
		sort(a+1,a+1+n);
		for(i=1;i<=n;i++)
		{
			rank[a[i].id]=i;
		}
		int ans=0;
       int circle=0,now=0;
	   memset(used,0,sizeof(used));
	   for(i=1;i<=n;i++)
		   if (i!=rank[i])
	   {
		   now=i;
		   circle=0;
		   while (!used[now])
		   {
			   circle++;
			   used[now]=true;
			   now=rank[now];
		   }
		   ans+=circle;
	   }
		printf("Case #%d: %d.000000\n",cas,ans);
	}
}