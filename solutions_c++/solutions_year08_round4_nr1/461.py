#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

#define M 11000

int dp[M][2];

int G[M],C[M],data[M];

int n,V,A,B;
void read_data()
{
	int i;
	scanf("%d%d",&n,&V);
	A = (n - 1) / 2;
	B = (n + 1) / 2;
	for (i=1;i<=A;i++) scanf("%d%d",&G[i],&C[i]);
	for (i=1;i<=B;i++) scanf("%d",&data[A + i]);
}

void init()
{
	int i;
	for (i=1;i<=B;i++)
	{
		dp[A + i][data[A + i]] = 0;
		dp[A + i][1 - data[A + i]] = -1;
	}
}

void update(int &s,int a)
{
	if (s == -1) s = a;
	else if (a != -1 && a < s) s = a;
}

void calc(int s,int v)
{
	if (s > A) return;
	calc(s << 1,1);  calc(s << 1,0);
	calc((s << 1) + 1,1);  calc((s << 1) + 1,0);
	dp[s][v] = -1;
	if (G[s])
	{
		if (v)
		{
			if (dp[s << 1][1] != -1 && dp[(s << 1) + 1][1] != -1) update(dp[s][v],dp[s << 1][1] + dp[(s << 1) + 1][1]);
		}
		else
		{
			if (dp[s << 1][0] != -1 && dp[(s << 1) + 1][0] != -1) update(dp[s][v],dp[s << 1][0] + dp[(s << 1) + 1][0]);
			if (dp[s << 1][0] != -1 && dp[(s << 1) + 1][1] != -1) update(dp[s][v],dp[s << 1][0] + dp[(s << 1) + 1][1]);
			if (dp[s << 1][1] != -1 && dp[(s << 1) + 1][0] != -1) update(dp[s][v],dp[s << 1][1] + dp[(s << 1) + 1][0]);
		}
	}
	else
	{
		if (v)
		{
			if (dp[s << 1][1] != -1 && dp[(s << 1) + 1][1] != -1) update(dp[s][v],dp[s << 1][1] + dp[(s << 1) + 1][1]);
			if (dp[s << 1][0] != -1 && dp[(s << 1) + 1][1] != -1) update(dp[s][v],dp[s << 1][0] + dp[(s << 1) + 1][1]);
			if (dp[s << 1][1] != -1 && dp[(s << 1) + 1][0] != -1) update(dp[s][v],dp[s << 1][1] + dp[(s << 1) + 1][0]);
		}
		else
		{
			if (dp[s << 1][0] != -1 && dp[(s << 1) + 1][0] != -1) update(dp[s][v],dp[s << 1][0] + dp[(s << 1) + 1][0]);
		}
	}

	if (C[s])
	{
		if (!G[s])
		{
			if (v)
			{
				if (dp[s << 1][1] != -1 && dp[(s << 1) + 1][1] != -1) update(dp[s][v],1 + dp[s << 1][1] + dp[(s << 1) + 1][1]);
			}
			else
			{
				if (dp[s << 1][0] != -1 && dp[(s << 1) + 1][0] != -1) update(dp[s][v],1 + dp[s << 1][0] + dp[(s << 1) + 1][0]);
				if (dp[s << 1][0] != -1 && dp[(s << 1) + 1][1] != -1) update(dp[s][v],1 + dp[s << 1][0] + dp[(s << 1) + 1][1]);
				if (dp[s << 1][1] != -1 && dp[(s << 1) + 1][0] != -1) update(dp[s][v],1 + dp[s << 1][1] + dp[(s << 1) + 1][0]);
			}
		}
		else
		{
			if (v)
			{
				if (dp[s << 1][1] != -1 && dp[(s << 1) + 1][1] != -1) update(dp[s][v],1 + dp[s << 1][1] + dp[(s << 1) + 1][1]);
				if (dp[s << 1][0] != -1 && dp[(s << 1) + 1][1] != -1) update(dp[s][v],1 + dp[s << 1][0] + dp[(s << 1) + 1][1]);
				if (dp[s << 1][1] != -1 && dp[(s << 1) + 1][0] != -1) update(dp[s][v],1 + dp[s << 1][1] + dp[(s << 1) + 1][0]);
			}
			else
			{
				if (dp[s << 1][0] != -1 && dp[(s << 1) + 1][0] != -1) update(dp[s][v],1 + dp[s << 1][0] + dp[(s << 1) + 1][0]);
			}
		}
	}
}

void work_dp()
{
	calc(1,0);
	calc(1,1);
}
void show_ans()
{
	if (dp[1][V] == -1) printf("IMPOSSIBLE\n");
	else printf("%d\n",dp[1][V]);
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t,i;
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		read_data();
		init();
		work_dp();
		fprintf(stderr,"%d\n",i);
		show_ans();
	}
	return 0;
}
