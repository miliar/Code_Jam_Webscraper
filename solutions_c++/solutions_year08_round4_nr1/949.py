#include <cstdio>
#include <algorithm>
#include <cstdlib>

using namespace std;


int m;
int a[16*1024];
int c[16*1024];
int dp[16*1024][2];
int v[16*1024];
bool u[16*1024][2];

int best(int a,int b)
{
	if(a <0)
		return b;
	if(b<0)
		return a;

	return min(a,b);
}

int calc_dp(int x,int w)
{
	if(x >= (m-1)/2)
		return (dp[x][w] = (a[x]==w ? 0 : -1));

	if(u[x][w])
		return dp[x][w];
	u[x][w] = true;

	int p[2] = { calc_dp(2*x+1,0), calc_dp(2*x+1,1) };
	int q[2] = { calc_dp(2*x+2,0), calc_dp(2*x+2,1) };

	int z = -100;
	int o = -100;
	int e = -100;

	if(p[0]>=0 && q[0]>=0)
		z = p[0] + q[0];

	if (p[0]>=0 && q[1]>=0 )
		o = p[0] + q[1];

	if (p[1]>=0 && q[0]>=0 )
		o = p[1] + q[0];

	if (p[1]>=0 && q[1]>=0 )
		e = p[1] + q[1];

	int r;
	if( a[x]==1 )
	{
		if( w==1 )
			r = c[x] ? best(e,o+1) : e;
		else
			r = best(z,o);
	}
	else
	{
		if(w==1)
			r = best(e,o);
		else
			r = c[x] ? best(z,o+1) : z;
	}

	dp[x][w] = r<0 ? -1 : r;

	return dp[x][w];
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int z=1;z<=t;z++)
	{
		int w;

		scanf("%d%d",&m,&w);

		int i;

		for(i=0;i<(m-1)/2;i++)
			scanf("%d%d",&a[i],&c[i]);

		for(;i<m;i++)
			scanf("%d",&a[i]);

		memset(u,0,sizeof(u));

		int r = calc_dp(0,w);

//		for(int i=0;i<m;i++)
//			printf("dp[%d][0]=%d dp[%d][1]=%d\n", i, dp[i][0], i, dp[i][1]);

		if( r==-1 )
			printf("Case #%d: IMPOSSIBLE\n",z);
		else
			printf("Case #%d: %d\n",z,r);
	}
	return 0;
}