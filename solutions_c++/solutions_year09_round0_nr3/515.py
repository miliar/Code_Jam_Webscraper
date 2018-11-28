#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

enum {SIZE = 505};

char s[SIZE], t[SIZE] = "welcome to code jam";
int dp[SIZE][SIZE], m, n;

void process(int tc)
{
	int ans, ndigs = 0;

	cin.getline(s, SIZE - 2);
	
	m = strlen(t);
	n = strlen(s);

	for(int i = 0; i < m; i++)
		for(int j = 0; j < n; j++)
			dp[i][j] = 0;

	dp[0][0] = (s[0] == t[0] ? 1 : 0);
	for(int i = 1; i < n; i++) 
		dp[0][i] = dp[0][i - 1] + (s[i] == t[0] ? 1 : 0);

	for(int i = 1; i < m; i++) 
		for(int j = i; j < n; j++) 
			dp[i][j] = (dp[i][j - 1] % 10000 + (s[j] == t[i] ? dp[i - 1][j - 1] : 0) % 10000) % 10000;

	ans = dp[m - 1][n - 1];

	while(dp[m - 1][n - 1] > 0) {
		ndigs++;
		dp[m - 1][n - 1] /= 10;
	}

	printf("Case #%d: ", tc);

	for(int i = 0; i < 4 - ndigs; i++)
		printf("0");

	if(ans == 0)
		printf("\n");
	else
		printf("%d\n", ans);
}

int main()
{
	int tc;

	scanf("%d", &tc);

	cin.getline(s, SIZE - 2);
	
	for(int i = 1; i <= tc; i++)
		process(i);

	return 0;
}

