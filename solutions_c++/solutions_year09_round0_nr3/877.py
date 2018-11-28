#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>

#define INF 1000000000
#define EPS 1E-8
#define PI 3.14159265358979
#define MOD 10000

using namespace std;

const char* welcome = "welcome to code jam";
char input[1000];
long dp[30][1000];

int main() {
	int n, len = strlen(welcome);
	cin >> n;
	gets(input);
	for(int t = 0; t < n; ++t) {
		gets(input);
		int ll = strlen(input);
		memset(dp, 0, 30 * 1000 * 4);
		for(int i = 0; i < ll; ++i) dp[0][i] = 1;
		for(int i = 0; i < ll; ++i) {
			for(int j = 0; j < len; ++j) {
				if(welcome[j] == input[i]) dp[j + 1][i + 1] = (dp[j + 1][i + 1] + dp[j][i]) % MOD;
				dp[j + 1][i + 1] = (dp[j + 1][i + 1] + dp[j + 1][i]) % MOD;
			}
		}
		printf("Case #%d: %04d\n", t + 1, dp[len][ll]);
	}
	return 0;
}
