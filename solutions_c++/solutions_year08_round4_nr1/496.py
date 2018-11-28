#include	<cstdio>
#include	<algorithm>
#define max(x,y) ((x)>(y)?(x):(y))
#define min(x,y) ((x)<(y)?(x):(y))
#define INF 1000000
using namespace std;
int n, t, v;
enum {OR, AND};
enum {NCHANGE, CHANGE};
int op[10000], c[10000];
int dp[10000][2];
void dfs (int i)
{
	if (i >= (n-1)/2)
		return;
	dfs (2*i+1);
	dfs (2*i+2);
	if (c[i] == NCHANGE) {
		if (op[i] == AND)
		{
			dp[i][0] <?= dp[2*i+1][0] + dp[2*i+2][1];
			dp[i][0] <?= dp[2*i+1][0] + dp[2*i+2][0];
			dp[i][0] <?= dp[2*i+1][1] + dp[2*i+2][0];
			dp[i][1] <?= dp[2*i+1][1] + dp[2*i+2][1];
		} else {
			dp[i][0] <?= dp[2*i+1][0] + dp[2*i+2][0];
			dp[i][1] <?= dp[2*i+1][1] + dp[2*i+2][1];
			dp[i][1] <?= dp[2*i+1][1] + dp[2*i+2][0];
			dp[i][1] <?= dp[2*i+1][0] + dp[2*i+2][1];			
		}
	} else {

		if (op[i] == AND)
		{
		//not change			
			dp[i][0] <?= dp[2*i+1][0] + dp[2*i+2][1];
			dp[i][0] <?= dp[2*i+1][0] + dp[2*i+2][0];
			dp[i][0] <?= dp[2*i+1][1] + dp[2*i+2][0];
			dp[i][1] <?= dp[2*i+1][1] + dp[2*i+2][1];
		//change
			dp[i][0] <?= dp[2*i+1][0] + dp[2*i+2][0] + 1;
			dp[i][1] <?= dp[2*i+1][1] + dp[2*i+2][1] + 1;
			dp[i][1] <?= dp[2*i+1][1] + dp[2*i+2][0] + 1;
			dp[i][1] <?= dp[2*i+1][0] + dp[2*i+2][1] + 1;	
		} else {
		//not change				
			dp[i][0] <?= dp[2*i+1][0] + dp[2*i+2][0];
			dp[i][1] <?= dp[2*i+1][1] + dp[2*i+2][1];
			dp[i][1] <?= dp[2*i+1][1] + dp[2*i+2][0];
			dp[i][1] <?= dp[2*i+1][0] + dp[2*i+2][1];	
		//change					
			dp[i][0] <?= dp[2*i+1][0] + dp[2*i+2][1] + 1;
			dp[i][0] <?= dp[2*i+1][0] + dp[2*i+2][0] + 1;
			dp[i][0] <?= dp[2*i+1][1] + dp[2*i+2][0] + 1;
			dp[i][1] <?= dp[2*i+1][1] + dp[2*i+2][1] + 1;		
		}		
		
	}
}
int main ()
{
	freopen ("A-large.in", "r", stdin);
	freopen ("std.txt", "w" ,stdout);
	scanf ("%d", &t);
	for (int l = 1; l <= t; ++ l)
	{
		memset (dp, 0, sizeof (dp));
		scanf ("%d %d", &n, &v);
		for (int i = 0; i < (n - 1) / 2; ++ i)
			scanf ("%d %d", &op[i], &c[i]);
		memset (dp, 0, sizeof(dp));
		int x;
		for (int i = 0; i < n; ++ i)
			for (int j = 0; j < 2; ++ j)
				dp[i][j] = INF;
		for (int i = (n - 1) / 2; i < n; ++ i)
		{
			scanf ("%d", &x);
			dp[i][x] = 0;
			dp[i][1-x] = INF;
		}
		printf ("Case #%d: ",l); 
		dfs (0);
		if (dp[0][v] == INF)
			puts ("IMPOSSIBLE");
		else
			printf ("%d\n", dp[0][v]);
	}
	//system ("pause");
}
