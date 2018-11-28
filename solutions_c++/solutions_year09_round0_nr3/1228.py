#include <cstdio>
#include <cstring>

int N;
int dp[505][20];
char str[] = "welcome to code jam";
char s[10000];

int main() {
	scanf("%d", &N); gets(s);
	for (int i=0;i<N;i++) {
		gets(s);
		memset(dp, 0, sizeof(dp));
		int j;
		if (s[0]=='w') dp[0][0]++;
		for (j=1;s[j];j++) {
			for (int k=0;k<19;k++) dp[j][k]=dp[j-1][k];
			if (s[j]=='w') dp[j][0]=(dp[j][0]+1)%10000;
			for (int k=1;k<19;k++) dp[j][k]=s[j]==str[k]?(dp[j][k]+dp[j][k-1])%10000:dp[j][k];
		}
		printf("Case #%d: %04d\n", i+1, dp[j-1][18]);
	}
	return 0;
}
