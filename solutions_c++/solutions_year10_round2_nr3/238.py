#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>

#include <iostream>
#include <sstream>
#include <string>

#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)

typedef pair<int,int> PII;
typedef long long ll;

#define MAXD 510

ll dp[MAXD][MAXD]; // n pos
ll res[MAXD];
ll choose[MAXD][MAXD];


void precompute()
{
	memset(dp, 0, sizeof(dp));
	memset(choose, 0, sizeof(choose));

	FOR (n, 0, MAXD) {
		choose[n][0] = 1;
		FOR (k, 1, n+1)
			choose[n][k] = (choose[n-1][k] + choose[n-1][k-1]) % 100003;
	}

	dp[1][0] = 1;
	
	FOR (n, 0, MAXD) {
		FOR (m, 1, n) {
			dp[n][m] = 0;
			FOR (d, 0, m) {
				dp[n][m] += dp[m][d]*choose[n-m-1][m-d-1];
				dp[n][m] %= 100003;
			}
		}
	}

	FOR (n, 0, MAXD) {
		ll sum = 0;
		FOR (d, 0, n)
			sum += dp[n][d];
		res[n] = sum % 100003;
	}
}

int main()
{
	precompute();

	ll T, c;
	scanf(" %lld", &T);
	FOR (i, 1, T+1) {
		scanf(" %lld", &c);
		printf("Case #%d: %lld\n", i, res[c]);
	}

	return 0;
}
