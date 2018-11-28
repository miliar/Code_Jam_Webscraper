#include<stdio.h>

#define INF 1000000000
int answer;
int r,n,req[2048];
int reqmax[2048];
int dp[1024][11];

int max(int a,int b)
{
	return a>=b?a:b;
}

void update(int&a,int b)
{
	if(b<a)a=b;
}

int f(int node,int sel)
{
	if(node>=n)return (sel>=req[node]?0:INF);
	if(dp[node][sel]!=-1)return dp[node][sel];
	dp[node][sel]=INF;
	update(dp[node][sel],f(node*2,sel+1)+f(node*2+1,sel+1)+req[node]);
	update(dp[node][sel],f(node*2,sel)+f(node*2+1,sel));
	return dp[node][sel];
}

void build(int node)
{
	if(node>=n){reqmax[node]=req[node];return;}
	build(node*2);
	build(node*2+1);
	reqmax[node]=max(reqmax[node*2],reqmax[node*2+1]);
}

void solve()
{
	int i,j;
	build(1);
	for(i=1;i<n;i++)
	{
		for(j=0;j<=r;j++)
		{
			dp[i][j]=(j>=reqmax[i]?0:-1);
		}
	}
	answer=f(1,0);
}

void input()
{
	int i,j;
	scanf("%d",&r);
	n=(1<<r);
	for(i=0;i<n;i++)
	{
		scanf("%d",&req[n+i]);
		req[n+i]=r-req[n+i];
	}
	for(i=r-1;i>=0;i--)
	{
		for(j=0;j<(1<<i);j++)
		{
			scanf("%d",&req[(1<<i)+j]);
		}
	}
}

int main()
{
	int t,T;
	scanf("%d",&t);
	for(T=1;T<=t;T++)
	{
		input();
		solve();
		printf("Case #%d: %d\n",T,answer);
	}
	return 0;
}
