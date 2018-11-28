#include <cstdio>
#include <cstdlib>
#include <cstring>

const char* message = "welcome to code jam";
const int M = 555;
const int D = 10000;
int dp[100];
char buffer[M];

int main(void) {
	int n;
	int m = strlen(message);
	dp[0] = 1;
	scanf("%d\n",&n);
	for (int in=1; in<=n; ++in) {
		fgets(buffer,M,stdin);
		for (int i=1; i<=m; ++i) dp[i]=0;
		for (int i=0; buffer[i]; ++i) {
			for (int j=m-1; j>=0; --j) {
				if (buffer[i] == message[j]) {
					dp[j+1] += dp[j];
					if (dp[j+1] >= D) dp[j+1] -= D;
				}
			}
		}
		printf("Case #%d: %04d\n",in,dp[m]);
	}
	return 0;
}
