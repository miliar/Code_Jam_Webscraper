#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <queue>

using namespace std;

FILE *fp_r, *fp_w;
int t;
char str[1000];
int dp[1000][20];
string base;
int len;

int main() {
	fp_r = fopen("c.in", "r");
	fp_w = fopen("c.out", "w");

	base = "welcome to code jam";

	fscanf(fp_r, "%d", &t);
	fgets(str, 1000, fp_r);
	for(int i = 0; i < t; ++i) {
		fgets(str, 1000, fp_r);

		memset(dp, 0, sizeof(dp));
		len = strlen(str);
		
		dp[0][0] = 1;
		for(int j = 1; j <= len; ++j) {
			for(int k = 0; k <= 19; ++k)
				dp[j][k] = dp[j-1][k];

			for(int k = 1; k <= 19; ++k) {
				if (str[j-1] != base[k-1]) continue;
				dp[j][k] = (dp[j][k] + dp[j-1][k-1]) % 10000;
			}
		}

		fprintf(fp_w, "Case #%d: %04d\n", i+1, dp[len][19]);
	}	

	fclose(fp_r);
	fclose(fp_w);

	return 0;
}