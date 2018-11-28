#include <stdio.h>
#include <string.h>

int size;
char text[509];
char str[30] = "welcome to code jam";
int dp[509][30];
int cas;

void solve() {
	int i,j;
	//scanf("%s",text);
	gets(text);
	for(i = 0; text[i] != '\0'; i++ ) {
		if (i == 0) {
			if (text[i] == str[0]) 
				dp[0][0] = 1;
			else
				dp[0][0] = 0;
			continue;
		}
		for(j = 0; str[j] != '\0';j++ ) {
			if(j == 0) {
				if(text[i] == str[j]) {
					dp[i][j] = dp[i - 1][j] + 1;
				} else {
					dp[i][j] = dp[i - 1][j];
				}
			} else {
				dp[i][j] = dp[i - 1][j];
				if(text[i] == str[j]) {
					dp[i][j] += dp[i - 1][j - 1];
				}
			}
			dp[i][j] %= 10000;
		}
	}
	printf("Case #%d: %04d\n",++cas,dp[i - 1][18]);
}

int main() {
	freopen("D:\\C-large.in","r",stdin);
	freopen("D:\\C-large.out","w",stdout);
	int i;
	char s[109];
	scanf("%d",&size);
	gets(s);
	for(i = 0; i < size; i++ ) {
		solve();
	}
}
