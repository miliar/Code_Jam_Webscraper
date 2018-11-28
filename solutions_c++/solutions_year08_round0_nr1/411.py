#include <stdio.h>
#include <string>
#include <map>

int min(int a, int b)
{
	return a < b ? a : b;
}
int min(int a, int b, int c)
{
	return min(min(a, b), c);
}

const int infty = 1000000;


int dp[1005][105];
int min1[105], min2[105];
int input[1005];

std::map<std::string, int> names;

void solve(int test_case)
{
	int n,m;
	scanf("%d\n", &n);
	char buf[200];
	names.clear();
	for(int i = 1; i <= n; i++)
	{
		gets(buf);
		names.insert(std::make_pair(std::string(buf), i));
	}
	scanf("%d\n", &m);
	for(int i = 1; i <= m; i++)
	{
		gets(buf);
		input[i] = names[std::string(buf)];
	}
	for(int i = 1; i <= n; i++)
		min1[i] = min2[i] = dp[0][i] = 0;
	min1[0] = infty;
	min2[n+1] = infty;

	for(int i = 1; i <= m; i++)
	{
		for(int j = 1; j <= n; j++)
			if (j == input[i])
				dp[i][j] = infty;
			else
				dp[i][j] = min(min1[j-1] + 1, dp[i-1][j], min2[j+1] + 1);
		for(int j = 1; j <= n; j++)
			min1[j] = min(min1[j-1], dp[i][j]);
		for(int j = n; j >= 1; j--)
			min2[j] = min(min2[j+1], dp[i][j]);
	}

	printf("Case #%d: %d\n", test_case, min2[1]);

	

}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
