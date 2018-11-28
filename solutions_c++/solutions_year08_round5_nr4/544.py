#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <set>
using namespace std;

#define M 210

int dp[M][M];
int n,m,R;
bool used[M][M];

void read_data()
{
	int a,b;
	cin >> n >> m >> R;
	int i;
	memset(used,false,sizeof(used));
	for (i=1;i<=R;i++)
	{
		cin >> a >> b;
		used[a][b] = true;
	}
}
void work_dp()
{
	memset(dp,0,sizeof(dp));
	dp[n][m] = 1;
	int i,j;
	for (i=n;i>=1;i--)
		for (j=m;j>=1;j--)
		{
			dp[i][j] += dp[i + 1][j + 2] + dp[i + 2][j + 1];
			dp[i][j] %= 10007;
			if (used[i][j]) dp[i][j] = 0;
		}
}

void show_ans()
{
	printf("%d\n",dp[1][1]);
}
int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int t;
	cin >> t;
	for (int i = 1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		read_data();
		work_dp();
		show_ans();
	}
	return 0;
}
