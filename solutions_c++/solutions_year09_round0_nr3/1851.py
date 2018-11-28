#include <cstdio>
#include <cstring>
using namespace std;

int main() {
	char s[501],w[20]="welcome to code jam";
	int N,L,i,j,testcase,dp[19];
	scanf("%d ",&N);
	for (testcase=1;testcase<=N;testcase++) {
		gets(s); L = strlen(s); memset(dp,0,19*sizeof(int));
		for (i=0;i<L;i++) {
			for (j=0;j<19;j++) {
				if (s[i] == w[j]) dp[j] += j ? dp[j-1] : 1;
				dp[j] %= 1000;
			}
		}
		printf("Case #%d: %04d\n",testcase,dp[18]);
	}
	return 0;
}
