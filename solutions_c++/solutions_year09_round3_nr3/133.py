#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define pi acos(-1.0)
#define inf (1<<30)
#define clr(a,b) memset(a,b,sizeof(a))
#define pb push_back

int dp[110][110],vi[110][110],c[110];

int func(int i,int j)
{
	if(vi[i][j])
		return dp[i][j];
	if(i>=j-1)
		return 0;
	int k,mn=inf,x;
	for(k=i+1;k<j;k++)
	{
		x=c[j]-c[i]-2;
		x+=func(i,k);
		x+=func(k,j);
		mn=min(mn,x);
	}
	vi[i][j]=1;
	dp[i][j]=mn;
	return dp[i][j];
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int l,n,i,r,cs,t=1;
	cin>>cs;
	while(cs--)
	{
		cin>>l;
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf("%d",&c[i]);
		}
		c[0]=0;
		c[n+1]=l+1;
		clr(dp,0);
		clr(vi,0);
		r=func(0,n+1);
		printf("Case #%d: %d\n",t++,r);
	}
	return 0;
}