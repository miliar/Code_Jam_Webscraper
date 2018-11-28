#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std; 
char s[] = "welcome to code jam";
char str[1000];
int main()
{
	int C,i,j,k,dp[1000],n,m;
	scanf("%d ", &C);
	for(k = 1;k <= C;k++) {
		fgets(str,999,stdin);
		n = strlen(str), m = strlen(s);
		memset(dp, 0, sizeof(dp));
		dp[0] = 1;
		for (i = 0; i < n; i++) {
			for (j = m; j > 0; j--) { 
				if (str[i] == s[j - 1])
					dp[j] = (dp[j] + dp[j - 1]) % 10000;
			}
		}
		printf("Case #%d: %04d\n", k, dp[m]);
	}
	return 0;
}
