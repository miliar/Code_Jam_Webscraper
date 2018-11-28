#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cstdio>
#include <string>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long LL;

const int codeType = 1;

const int MAXN = 20;
const int MAXM = 512;
const int MODD = 10000;

string pat = "welcome to code jam";

char str[MAXM];
int dp[MAXM], len1, len2;

int main()
{
	int cas;

	if(codeType == 0) {
		freopen("C-small-attempt0.in", "r", stdin);
		freopen("C-small.out", "w", stdout);
	}
	else if(codeType == 1) {
		freopen("C-large.in", "r", stdin);
		freopen("C-large.out", "w", stdout);
	}
	else {
		freopen("input.txt", "r", stdin);
	}

	scanf("%d%*c", &cas);
	for(int c = 1; c <= cas; c ++) {
		gets(str);

		memset(dp, 0, sizeof(dp));

		dp[0] = 1;
		len1 = strlen(str);
		len2 = pat.length();
		for(int i = 1; i <= len1; i ++) {
			for(int j = len2; j >= 1; j --) {
				if(str[i - 1] == pat[j - 1]) {
					dp[j] = (dp[j] + dp[j - 1]) % MODD;
				}
			}
		}

		printf("Case #%d: %04d\n", c, dp[len2]);
	}

	return 0;
}