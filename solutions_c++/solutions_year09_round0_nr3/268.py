#include <cstdio>
#include <algorithm>
using namespace std;

const char W[] = "welcome to code jam";
const int MOD = 10000;

int main()
{
	char str[512];
	int T;
	scanf("%d\n", &T);
	for(int t = 0; t < T; t++) {
		gets(str);
		int dp[20] = { 1 };
		for(int i = 0; str[i] != 0; i++) for(int j = 19; j > 0; j--)
			if(str[i] == W[j-1]) dp[j] = (dp[j]+dp[j-1])%MOD;
		printf("Case #%d: %04d\n", t+1, dp[19]);
	}
	return 0;
}

